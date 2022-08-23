from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=10)
    cpf = models.CharField(max_length=15)
    idade = models.IntegerField()
    dt_nasc = models.DateField()

    def __str__(self):
        return self.nome


# class Curso(models.Model):
#     NIVEL = (("B", "Básico"), ("I", "Intermediário"), ("A", "Avançado"))
#     cd_curso = models.CharField(max_digits=10)
#     descricao = models.CharField(max_digits=100)
#     nivel = models.CharField(
#         max_length=1, choices=NIVEL, blank=False, null=False, default="B"
#     )

#     def __str__(self):
#         return self.descricao
