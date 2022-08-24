from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ("id", "nome", "rg", "cpf", "idade")

    def create(self, validated_data):
        return super().create(validated_data)
