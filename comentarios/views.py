from urllib import request

from django.shortcuts import render

from comentarios.models import Comentario

from comentarios.serializers import ComentarioSerializer
from publicaciones.serializers import  PublicacionSerializer

from publicaciones.models import Publicacion
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
# Create your views here



class ComentarioViewSet(viewsets.ModelViewSet):
   queryset = Comentario.objects.all()
   serializer_class = ComentarioSerializer
   permission_classes = (AllowAny, )

   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def publicaciones (self, request, pk=None):
      comentario= self.get_object()

      if request.method == 'GET':
         serializer =  PublicacionSerializer(comentario.tag, many=True)
         return Response(status=status.HTTP_200_OK, data=serializer.data)

   @action(methods=['GET', 'POST', 'DELETE'], detail=True)
   def publicaciones(self, request, pk=None):
      comentarios = self.get_object()
      if request.method == 'GET':
         serialized = PublicacionSerializer(comentarios.publicaciones, many=True)
         return Response(status=status.HTTP_200_OK, data=serialized.data)

      if request.method == 'POST':
         public_id = request.data['publicaciones_ids']

         for id_com in public_id:
            try:

               publicacion = Publicacion.objects.get(id=id_com)
               comentarios.publicaciones.add(publicacion)

            except:
                return Response(status=status.HTTP_404_NOT_FOUND)


         serializer = PublicacionSerializer(comentarios.publicaciones, many=True)
         return Response(status=status.HTTP_201_CREATED, data=serializer.data)

      if request.method == 'DELETE':

          public_id = request.data['publicaciones_ids']

          for id_com in public_id:
              try:

                  publicacion = Publicacion.objects.get(id=id_com)
                  comentarios.publicaciones.remove(publicacion)

              except:
                  return Response(status=status.HTTP_404_NOT_FOUND)

          serializer = PublicacionSerializer(comentarios.publicaciones, many=True)
          return Response(status=status.HTTP_201_CREATED, data=serializer.data)
