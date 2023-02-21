from rest_framework.authentication import get_authorization_header # Retorna la variable autorization
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .authentication import ExpireTokenAuthenticattion


class Authentication(object):
    user = None
    user_token_expired = False

    def get_user(self, request):
        token = get_authorization_header(request).split()  # Get de header variable

        if token:
            try:
                token = token[1].decode() #
            except:
                return None
            
            token_expire = ExpireTokenAuthenticattion()
            user, token, message, self.user_token_expired = token_expire.authenticate_credentials(token)

            if user != None and token != None:
                return user
            return message
        return None

    
    def dispatch(self, request, *args, **kwargs):
        user = self.get_user(request)

        if user is not None:
            if type(user) == str:
                response =  Response({'error': user, 'token_expired':self.user_token_expired}, status=status.HTTP_401_UNAUTHORIZED)
                response.accepted_renderer = JSONRenderer()
                response.accepted_media_type = 'applicatiion/json'
                response.renderer_context = {}
                return response

            if not self.user_token_expired:
                return super().dispatch(request, *args, **kwargs)
        
        response = Response({'error': 'No e han envíado las credenciales.', 'token_expired':self.user_token_expired}, status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'applicatiion/json'
        response.renderer_context = {}
        return response
    