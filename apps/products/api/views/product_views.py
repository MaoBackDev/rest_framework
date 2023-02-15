from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.product_serializers import ProductSerializer


class ProductsAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'El producto se ha creado de manera satisfactoria !'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsActionsAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def patch(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()

        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {'error': 'No existe un producto con los datos proporciandos'},
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()

        if product:
            product_serializer = self.serializer_class(product, data=request.data)

            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message': 'Producto actualizado'}, status=status.HTTP_200_OK)

            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()

        if product:
            product.state = False
            product.save()
            return Response(
                {'message': 'El producto ha sido eliminado !'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'error': 'No existe un producto con los datos proporciandos'},
            status=status.HTTP_400_BAD_REQUEST
        )



# class ProductListAPIView(GeneralListAPIView):
#     serializer_class = ProductSerializer
#
# class ProductCreatetAPIView(generics.CreateAPIView):
#     serializer_class = ProductSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 {'message': 'El producto se ha creado de manera satisfactoria !'},
#                 status=status.HTTP_201_CREATED
#             )
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductRetrieveAPIView(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
#
#     def get(self, request, pk=None):
#         product = self.get_serializer().Meta.model.objects.filter(id=pk).first()
#
#         if product:
#             product_serializer = self.serializer_class(product)
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {'message': 'Producto no encontrado'},
#                 status=status.HTTP_404_NOT_FOUND
#             )
#
#
# class ProductDestroyAPIView(generics.DestroyAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
#
#     def delete(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#
#         if product:
#             product.state = False
#             product.save()
#             return Response(
#                 {'message': 'El producto ha sido eliminado !'},
#                 status=status.HTTP_200_OK
#             )
#         else:
#             return Response(
#                 {'error': 'No existe un producto con los datos proporciandos'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     serializer_class = ProductSerializer
#
#     def get_queryset(self):
#         return self.get_serializer().Meta.model.objects.filter(state=True)
#
#     def patch(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#
#         if product:
#             product_serializer = self.serializer_class(product)
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {'error': 'No existe un producto con los datos proporciandos'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def put(self, request, pk=None):
#         product = self.get_queryset().filter(id=pk).first()
#
#         if product:
#             product_serializer = self.serializer_class(product, data=request.data)
#
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 return Response({'message': 'Producto actualizado'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response(
#             {'error': 'No existe un producto con los datos proporciandos'},
#             status=status.HTTP_400_BAD_REQUEST
#         )