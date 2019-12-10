from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

urlpatterns = [
    path('', views.AllUsers.as_view(), name='users'),
    path('login/', obtain_auth_token, name='login'),
]