from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class ContactForm(serializers.Serializer):
    # simple serializer for emails
    email = serializers.EmailField()
    message = serializers.CharField()


# simple endpoint to take the serializer data
class SendEmail(APIView):
    # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=ContactForm)
    def post(self, request):
        # serializer object
        serializer = ContactForm(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
