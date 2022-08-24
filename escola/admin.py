from django.contrib import admin

from escola.models import Aluno, Curso


class Alunos(admin.ModelAdmin):
    list_display = ("id", "nome", "rg", "cpf", "dt_nasc")
    list_display_links = ("id", "nome")
    search_fields = (
        "nome",
        "cpf",
    )
    list_per_page: 10


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ("id", "cd_curso", "descricao", "nivel")
    list_display_links = ("id", "cd_curso")
    search_fields = ("cd_curso",)
    list_per_page: 10


admin.site.register(Curso, Cursos)
