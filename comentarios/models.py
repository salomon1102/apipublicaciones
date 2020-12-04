import datetime
from django.db import models


class Comentario(models.Model):
    comentario = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.comentario