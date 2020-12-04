from django.shortcuts import render
from comentarios.models import  Comentario
from comentarios.serializers import ComentarioSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here
# .
class ComentarioViewSet(viewsets.ModelViewSet):
   queryset = Comentario.objects.all()
   serializer_class = ComentarioSerializer
   permission_classes = (AllowAny, )