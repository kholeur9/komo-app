from django.urls import path
from .views import excel_data

urlpatterns = [
  path('', excel_data, name='administrateur'),
]