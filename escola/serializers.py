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


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()  # faz retornar a partir de um método

    class Meta:
        model = Matricula
        fields = ("curso", "periodo")

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source="alunos.nome")

    class Meta:
        model = Matricula
        fields = ["aluno_nome"]
