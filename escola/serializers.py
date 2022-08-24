from rest_framework import serializers
from .models import Aluno, Curso, Matricula
from rest_framework.status import HTTP_400_BAD_REQUEST


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ("id", "nome", "rg", "cpf", "idade")

    def create(self, validated_data):
        dup_cpf = self.Meta.model.objects.filter(cpf=validated_data["cpf"]).exists()
        dup_rg = self.Meta.model.objects.filter(rg=validated_data["rg"]).exists()
        if dup_cpf or dup_rg:
            return HTTP_400_BAD_REQUEST
        return super().create(validated_data)


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data)


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ("id", "aluno", "curso", "periodo")

    def create(self, validated_data):
        return super().create(validated_data)
