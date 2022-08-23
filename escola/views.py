from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, "index.html")


def alunos(request):
    if request.method == "GET":
        alunos_list = {"id": 1, "Nome": "Thiago", "Sobrenome": "Kasper", "Idade": "20"}
        return JsonResponse(alunos_list)
