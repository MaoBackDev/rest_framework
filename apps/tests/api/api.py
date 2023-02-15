# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from apps.tests.models import Test
from .serializers import *


# APIView 
# class TestAPIView(APIView):
#     def get(self, request):
#         tests = Test.objects.all()
#         test_serializer = TestSerializer(tests, many=True)
#         return Response(test_serializer.data)

#     def post(self, request):
#         test_serializer = TestSerializer(data=request.data)
#         if test_serializer.is_valid():
#             test_serializer.save()
#             return Response(test_serializer.data)
#         return Response(test_serializer.errors)



# API usando funciones y decoradores
@api_view(['GET', 'POST'])
def test_api_view(request):

    # READ LIST
    if request.method == 'GET':

        # QUERYSET
        tests = Test.objects.all()
        tests_serializer = TestSerializer(tests, many=True)

        # Este es contenido de prueba
        # test_data = {
        #     'title': 'Contenido de prueba',
        #     'content': 'Este es un contenido de prueba para validar serializers'
        # }
        # new_serializer = NewTestSerializer(data=test_data, context=test_data)

        # if new_serializer.is_valid():
        #     test_instance = new_serializer.save()
        #     print(test_instance)
        # else:
        #     print(new_serializer.errors)  # FIN DEL CONTENIDO DE PRUEBA

        return Response(tests_serializer.data, status=status.HTTP_200_OK)

    # CREATE
    elif request.method == 'POST':

        # QUERYSET
        test_serializer = TestSerializer(data=request.data)

        # VALIDATION
        if test_serializer.is_valid():
            test_serializer.save()
            return Response(
                {'message': 'El test se ha creado exitosamente !'}, 
                status=status.HTTP_201_CREATED
            )
        return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def test_detail_api_view(request, pk=None):
    # QUERYSET
    test = Test.objects.filter(id=pk).first()  # Retorna el elemento -- funciona como un get

    # VALIDATION
    if test:
        
        # RETRIEVE OR DETAIL
        if request.method == 'GET':
            test_serializer = TestSerializer(test)
            return Response(test_serializer.data, status=status.HTTP_200_OK)

        # UPDATE
        elif request.method == 'PUT':
            test_serializer = TestSerializer(test, data=request.data)
            # test_serializer = NewTestSerializer(test, data=request.data)

            if test_serializer.is_valid():
                test_serializer.save()

                return Response(
                    {'message': f'el test {test.title} ha sido actualizado correctamente !'}, 
                    status=status.HTTP_200_OK
                )

            return Response(test_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # DELETE
        elif request.method == 'DELETE':
            test.delete()
            return Response(
                {'message': f'El test {test.title} fue eliminado'}, 
                status=status.HTTP_200_OK
            )

    return Response(
        {'message': 'No se ha encontrado un test con los datos proporciandos'},
        status = status.HTTP_404_NOT_FOUND
    )