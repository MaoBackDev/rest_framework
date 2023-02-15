from django.urls import path

from .api import *

urlpatterns = [
    path('', test_api_view, name='def_test_api'),
    path('<int:pk>/', test_detail_api_view, name='test_detail'),
    # path('new/', new_api_view, name='new'),
]