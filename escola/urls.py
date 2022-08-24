from django.urls import path

from escola.views import AlunoList, AlunoDetail, CursoList, CursoDetail

urlpatterns = [
    path("alunos/", AlunoList.as_view(), name="AlunoList"),
    path("alunos/create/", AlunoDetail.as_view(), name="AlunoDetail"),
    path("cursos/", CursoList.as_view(), name="CursoList"),
    path("cursos/create/", CursoDetail.as_view(), name="CursoDetail"),
]
