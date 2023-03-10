from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpireTokenAuthenticattion(TokenAuthentication):
    expired = False

    def expires_in(self, token):
        """
        Calcula el tiempo de vida qeu tendrá un token
        """
        time_elapsed = timezone.now() - token.created  # Tiempo transcurrido desde la creación del token
        left_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time
    
    def is_token_expired(self, token):
        """Valida que el tiempo del token halla expirado"""
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expired_handler(self, token):
        """Valida que el token haya expirado"""
        is_expire = self.is_token_expired(token)

        if is_expire:
            self.expired = True
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)
        
        return is_expire, token

    def authenticate_credentials(self, key):
        message, token, user = None, None, None

        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            user = token.user

        except self.get_model().DoesNotExist:
            message = 'Token Inválido.'
            self.expired = True
        
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario Ináctivo o eliminado.'
            
            is_expired = self.token_expired_handler(token)

            if is_expired:
                message = 'Su token ha expirado.'
        
        return (user, token, message, self.expired)