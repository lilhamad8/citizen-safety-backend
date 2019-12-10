from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import CustomUser
from rest_framework.permissions import IsAuthenticated

class AllUsers(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        # content = CustomUser.objects.all()
        content = {'message': 'Hello, World!'}
        return Response(content)
