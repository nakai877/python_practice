from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('home2/', views.home2, name='home2'),
    path('', views.hello, name='hello'),
    path('home/', views.home, name='home'),
    path('home3/', views.Home.as_view(), name='home3')
]

