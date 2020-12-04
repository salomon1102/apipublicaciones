from django.shortcuts import render
from tags.models import  Tag
from tags.serializers import TagSerializer
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here
# .
class TagViewSet(viewsets.ModelViewSet):
   queryset = Tag.objects.all()
   serializer_class = TagSerializer
   permission_classes = (AllowAny, )