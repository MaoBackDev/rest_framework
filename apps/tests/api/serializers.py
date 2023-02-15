from rest_framework import serializers

from apps.tests.models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class NewTestSerializer(serializers.Serializer):
    """Custom sertializer don't need a model"""
    title = serializers.CharField(max_length = 255)
    content = serializers.CharField

    # VALIDAR UN SERIALIZER DE MANERA PERSONALIZADA
    def validate_title(self, value):
        
        if len(value) < 6:
            raise serializers.ValidationError('El título debe tener más de 15 caracteres !')
        return value

    def create(self, validate_data):
        print(f'DATA VALIDADA:\n{validate_data}')
        return Test.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.content = validate_data.get('content', instance.content)
        instance.save()
        return instance

    # El método save()  afecta directamente al modelo
    # def save(self):
    #     print(self)


    # def validate_email(self, value):
    #     if '@' not in value or '.com' not in value:
    #         raise serializers.ValidationError('Debe proporcionar un correo válido !')
        
    #     if self.validate_title(self.initial_data['title']) in value:
    #         raise serializers.ValidationError('El correo no puede tener el nombre de usuario !')
    #     return value

    

    # def validate(self, data):
    #     if data['title'] in data['email']:
    #         raise serializers.ValidationError('El correo no puede tener el nombre de usuario !')
    #     return data

