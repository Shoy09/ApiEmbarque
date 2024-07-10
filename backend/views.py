from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

#------------Usuario--------------------
from rest_framework.views import APIView
class UserListCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#------------token--------------------

@api_view(['POST'])
@parser_classes([JSONParser, FormParser])
def obtain_tokens(request):
    if request.method == 'POST':
        dni = request.data.get('dni')
        password = request.data.get('password')

        # Validación básica de los datos de entrada
        if not dni or not password:
            return Response({'error': 'Debe proporcionar DNI y contraseña.'}, status=status.HTTP_400_BAD_REQUEST)

        # Autenticación del usuario
        user = authenticate(request, username=dni, password=password)

        if user is None:
            return Response({'error': 'Credenciales inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generar tokens de acceso y refresh
        refresh = RefreshToken.for_user(user)
        tokens = {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

        return Response(tokens, status=status.HTTP_200_OK)
    

# DIARIO DE PESCA
class DiarioPescaCrud(viewsets.ModelViewSet):
    queryset = DiarioDePesca.objects.all()
    serializer_class = DiarioDePescaSerializer