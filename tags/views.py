from django.shortcuts import render
from tags.models import  Tag
from tags.serializers import TagSerializer
from comentarios.serializers import ComentarioSerializer
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


   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def publicaciones(self, request, pk=None):
      comentario = self.get_object()

      if request.method == 'GET':
         serializer =  ComentarioSerializer(comentario.publicacion, many=True)
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

   
