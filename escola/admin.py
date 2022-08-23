from django.contrib import admin

from escola.models import Aluno


class Alunos(admin.ModelAdmin):
    list_display = ("id", "nome", "rg", "cpf", "dt_nasc")
    list_display_links = ("id", "nome")
    search_fields = (
        "nome",
        "cpf",
    )
    list_per_page: 10


admin.site.register(Aluno, Alunos)
