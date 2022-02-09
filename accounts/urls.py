from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken


app_name = 'accounts'

urlpatterns = [
    path('token/', ObtainAuthToken.as_view(), name='obtain-token'),
]