from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.CorporateContactCreate.as_view(), name='corporate_create')
]

