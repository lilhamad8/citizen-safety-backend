from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.models import CustomUser
from user.serializer import UserSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers

@csrf_exempt
@api_view(["POST"])
# @permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username)
    print(password)
    if username is None or password is None:
        return Response({'error': 'Please provide both email and password'},
                        status=HTTP_400_BAD_REQUEST)
    try:
        user = CustomUser.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
    except CustomUser.DoesNotExist:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    # user = UserSerializer(user)

    # user = serializers.serialize('json', [ user, ], fields=('first_name','last_name','phone','location'))
    data = {}
    data["first_name"]=user.first_name
    data["last_name"]=user.last_name
    data["phone"]=user.phone
    data["email"]=user.email
    # data["response"]={'token': token.key,'user':user}
    # return JsonResponse({'foo': 'bar'})
    return JsonResponse({'data':{'token': token.key,'user':data}}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        CustomUser.objects.create_user(
            serialized.save()
        )
        print('done')
        return Response(serialized.data, status=HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=HTTP_400_BAD_REQUEST)


class AllUsers(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        # content = CustomUser.objects.all()
        content = {'message': 'Hello, World!'}
        return Response(content)


        
