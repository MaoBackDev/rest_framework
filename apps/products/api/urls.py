from django.urls import path

from apps.products.api.views.general_views import *
from apps.products.api.views.product_viewset import *



urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('Indicator_product/', IndicatortListAPIView.as_view(), name='Indicator_product'),
    # path('product/', ProductsAPIView.as_view(), name='products'),
    # path('product/<int:pk>/', ProductsActionsAPIView.as_view(), name='actions'),
    # path('product/create/', ProductCreatetAPIView.as_view(), name='create'),
    # path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='detail'),
    # path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='destroy'),
    # path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update'),
]