from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    def update(self, instance, validate_data):
        user = super().update(instance, validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        """Define la representación de un objeto, es decir los campos quye se mestran en un listado
           No aplica para el método save, este seguirá usando todos los campos obligatrios.
           Se pueden personalizar los campos que se verán en el resultado.
           IMPORTANTE: se deben pasar los parámetros en la consulta con el método values()"""

        return {
            'id': instance['id'],
            'nombres': instance['first_name'],
            'apellidos': instance['last_name'],
            'correo': instance['email'],
            'contraseña': instance['password']
        }
    

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']