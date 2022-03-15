from django.shortcuts import render
from rest_framework import viewsets, status, generics , permissions, authentication

# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import NewUser
from .serializers import  CustomUserSerializer


class UserGCList(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination


class UserGCDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer

class UserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#////////////////////////////
class UserViewset(viewsets.ViewSet):
    def list(self,request):
        users = NewUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET','POST'])
def apifunction(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = NewUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)

        items = {
            "items": serializer.data
        }

        return Response(items)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = NewUser.objects.get(pk=pk)
    except NewUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)