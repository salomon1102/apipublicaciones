from django.shortcuts import render


from publicaciones.models import Publicacion
from tags.models import Tag
from tags.serializers import TagSerializer
from publicaciones.serializers import PublicacionSerializer
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
    permission_classes = (AllowAny,)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicacion (self, request, pk=None):
       tag = self.get_object()

       if request.method == 'GET':
          serializer = PublicacionSerializer(tag.publicaciones_tag, many=True)
          return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicacion(self, request, pk=None):
       tag = self.get_object()

       if request.method == 'GET':
          serializer = PublicacionSerializer(tag.publicaciones_tag, many=True)
          return Response(status=status.HTTP_200_OK, data=serializer.data)

       if request.method == 'POST':
          comet_id = request.data['publicaciones_ids']


          for id_com in comet_id:
             publicacion = Publicacion.objects.get(id=id_com)
             tag.publicaciones_tag.add(publicacion)

          serializer = PublicacionSerializer(tag.publicaciones_tag, many=True)
          return Response(status=status.HTTP_200_OK, data=serializer.data)

       if request.method == 'DELETE':
          comet_id = request.data['publicaciones_ids']

          for id_com in comet_id:
             publicaciones = Publicacion.objects.get(id=id_com)
             tag.publicaciones_tag.add(publicaciones)

          serializer = PublicacionSerializer(tag.publicaciones_tag, many=True)
          return Response(status=status.HTTP_200_OK, data=serializer.data)
