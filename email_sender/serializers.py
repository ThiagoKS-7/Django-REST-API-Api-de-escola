from rest_framework import serializers
from email_sender.models import Email


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ("id", "remetente", "assunto", "mensagem")

    def create(self, validated_data):
        return super().create(validated_data)
