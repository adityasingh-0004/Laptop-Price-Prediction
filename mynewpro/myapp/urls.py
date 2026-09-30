from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReadCSV, name='ReadCSV'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('housePrediction/',views.housePrediction,name='housePrediction')
]