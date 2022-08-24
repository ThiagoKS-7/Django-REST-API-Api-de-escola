from django.shortcuts import render, redirect
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer
from escola.models import Aluno, Curso, Matricula
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny


def index(request):
    return redirect("api")


def api(request):
    return render(request, "index.html")


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    # faz com que o get traga com ?search='pesquisa', comparando com esses campos
    search_fields = ("nome", "cpf")


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ("descricao", "nivel")


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = (AllowAny,)


"""
Quando precisar desabilitar um método dos viewsets:
* https://stackoverflow.com/questions/23639113/disable-a-method-in-a-viewset-django-rest-framework
"""
