from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AlunoSerializer, CursoSerializer
from escola.models import Aluno, Curso
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema


def index(request):
    return redirect("api")


def api(request):
    return render(request, "index.html")


class AlunoList(APIView):
    def get(self, request, format=None):
        Alunos = Aluno.objects.all()
        serializer = AlunoSerializer(Alunos, many=True)  # o many é True qnd for lista
        return Response(serializer.data, status=HTTP_200_OK)


class AlunoDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=AlunoSerializer)
    def post(self, request, format=None):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validação - formato de email inválido",
            },
            status=HTTP_400_BAD_REQUEST,
        )


class CursoList(APIView):
    def get(self, request, format=None):
        Cursos = Curso.objects.all()
        serializer = CursoSerializer(Cursos, many=True)  # o many é True qnd for lista
        return Response(serializer.data, status=HTTP_200_OK)


class CursoDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=CursoSerializer)
    def post(self, request, format=None):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houveram erros de validação - formato de email inválido",
            },
            status=HTTP_400_BAD_REQUEST,
        )
