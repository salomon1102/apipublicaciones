from rest_framework import serializers

from comentarios.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comentario
        fields = '__all__'
        #fields = ('nombre','direccion',)