from django.shortcuts import render
from publicaciones.models import  Publicacion
from publicaciones.serializers import PublicacionSerializer
from comentarios.serializers import ComentarioSerializer
from tags.serializers import TagSerializer
from comentarios.models import  Comentario

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

   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def tags(self, request, pk=None):
      publicacion = self.get_object()

      if request.method == 'GET':
         serializer = TagSerializer(publicacion.tag, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)

   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def comentarios(self, request, pk=None):
      publicacion = self.get_object()

      if request.method == 'GET':
         serializer = ComentarioSerializer(publicacion.comentarios, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)

      if request.method == 'POST':
         comet_id = request.data['comentarios_ids']

         for id_com in comet_id:
            comentario = Comentario.objects.get(id=id_com)
            publicacion.comentarios.add(comentario)

         serializer = ComentarioSerializer(publicacion.comentarios, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)
   
      if request.method == 'DELETE':
         comet_id = request.data['comentarios_ids']

         for id_com in comet_id:
            comentario = Comentario.objects.get(id=id_com)
            publicacion.comentarios.remove(comentario)

         serializer = ComentarioSerializer(publicacion.comentarios, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)
