from django.shortcuts import render
from publicaciones.models import  Publicacion
from publicaciones.serializers import PublicacionSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here
# .
class PublicacionViewSet(viewsets.ModelViewSet):
   queryset = Publicacion.objects.all()
   serializer_class = PublicacionSerializer
   permission_classes = (AllowAny, )