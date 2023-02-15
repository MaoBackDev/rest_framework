from rest_framework import generics

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import * 


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer


class IndicatortListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer