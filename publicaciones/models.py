import datetime

from django.db import models
from comentarios.models import Comentario
from tags.models import Tag


class Publicacion(models.Model):
    usuario = models.CharField(max_length=200)
    publicacion = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.datetime.now(),null=True)

    comentarios = models.ManyToManyField(Comentario, related_name='publicaciones')
    tag = models.ManyToManyField(Tag, related_name='publicaciones_tag')

    def __str__(self):
        return self.usuario