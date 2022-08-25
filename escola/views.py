from django.shortcuts import render, redirect
from .serializers import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
)
from escola.models import Aluno, Curso, Matricula
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny


def index(request):
    return redirect("api")


def api(request):
    return render(request, "index.html")


class AlunoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    # faz com que o get traga com ?search='pesquisa', comparando com esses campos
    search_fields = ("nome", "cpf")


class CursoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (AllowAny,)
    filter_backends = (SearchFilter,)
    search_fields = ("descricao", "nivel")


class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = (AllowAny,)


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando todas as matrículas de cada aluna e aluno"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


"""
Quando precisar desabilitar um método dos viewsets:
* https://stackoverflow.com/questions/23639113/disable-a-method-in-a-viewset-django-rest-framework
"""
