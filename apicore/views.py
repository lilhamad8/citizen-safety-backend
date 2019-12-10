from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import CustomUser

class AllUser(APIView):
    def get(self, request):
        content = CustomUser.objects.all()
        return Response(content)
