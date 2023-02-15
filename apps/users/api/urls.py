from django.urls import path

from .api import *


urlpatterns = [
    # path('', UserAPIView.as_view(), name='user_api'),
    path('', user_api_view, name='users'),
    path('<int:pk>/', get_user_api_view, name='get_user'),
    
]