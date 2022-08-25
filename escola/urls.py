from django.urls import include, path
from rest_framework import routers

from escola.views import (
    AlunoViewSet,
    CursoViewSet,
    MatriculaViewSet,
    ListaMatriculasAluno,
    ListaAlunosCurso,
)

router = routers.DefaultRouter()

router.register(r"alunos", AlunoViewSet, basename="Aluno")
router.register(r"cursos", CursoViewSet, basename="Curso")
router.register(r"matriculas", MatriculaViewSet, basename="Matricula")

urlpatterns = [
    path("", include(router.urls)),
    path(
        r"aluno/<int:pk>/matriculas/",
        ListaMatriculasAluno.as_view(),
        name="MatriculasAluno",
    ),
    path(
        r"curso/<int:pk>/matriculas/",
        ListaAlunosCurso.as_view(),
        name="AlunosCurso",
    ),
]
