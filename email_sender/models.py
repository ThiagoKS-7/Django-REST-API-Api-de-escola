from django.db import models


class Email(models.Model):
    remetente = models.EmailField(max_length=255)
    assunto = models.CharField(max_length=255)
    mensagem = models.CharField(max_length=500)
