from rest_framework import serializers
from .models import Aluno, Curso


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ("id", "nome", "rg", "cpf", "idade")

    def create(self, validated_data):
        return super().create(validated_data)


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ("cd_curso", "descricao", "nivel")

    def create(self, validated_data):
        return super().create(validated_data)
