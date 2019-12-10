from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from . import views

urlpatterns = [
    # 'users' test endpoint
    path('', views.AllUsers.as_view(), name='users'), 
    path('login/', views.login, name='login'),
    path('signup/', views.create_user, name='signup'),
]