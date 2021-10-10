from rest_framework import generics, status, permissions
from rest_framework.response import Response

from users.serializers import SignUpSerializer


class SignUp(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SignUpSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            "user": self.serializer_class(user, context=self.get_serializer_context()).data
        }
        return Response(data, status=status.HTTP_201_CREATED)
