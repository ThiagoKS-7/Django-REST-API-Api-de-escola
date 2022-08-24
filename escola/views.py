from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AlunoSerializer
from escola.models import Aluno
from rest_framework.status import HTTP_200_OK


def index(request):
    return redirect("api")


def api(request):
    return render(request, "index.html")


class AlunosList(APIView):
    def get(self, request, format=None):
        Alunos = Aluno.objects.all()
        serializer = AlunoSerializer(Alunos, many=True)  # o many é True qnd for lista
        return Response(serializer.data, status=HTTP_200_OK)
