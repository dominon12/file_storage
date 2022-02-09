from django.urls import path

from . import views


app_name = 'files'

urlpatterns = [
    path('image/', views.ImageListOrCreate.as_view(), name='image-list-or-create'),
    path('image/<pk>/', views.ImageDetailOrDelete.as_view(), name='image-detail-or-delete'),
]