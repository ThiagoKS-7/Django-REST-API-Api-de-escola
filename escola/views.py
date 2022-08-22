from django.http import JsonResponse


def alunos(request):
    if request.method == "GET":
        alunos_list = {"id": 1, "Nome": "Thiago", "Sobrenome": "Kasper", "Idade": "20"}
        return JsonResponse(alunos_list)
