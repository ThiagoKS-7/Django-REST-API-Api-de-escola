from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from email_sender.serializers import EmailSerializer


# simple endpoint to take the serializer data
class SendEmail(APIView):
    # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=EmailSerializer)
    def post(self, request):
        # serializer object
        serializer = EmailSerializer(data=request.data)
        # checking for errors
        if serializer.is_valid():
            author = "multistackdjango@gmail.com"
            json = serializer.data
            send_mail(json["assunto"], json["mensagem"], author, [json["remetente"]])
            return Response(
                data={"status": "OK", "data": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
