from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response

from applications.account.serializers import RegisterSerializer

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией', status=201)
    

class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
        except User.DoesNotExist:
            return Response('Нет такого кода!', status=200)
        return Response('Успешно', status=200)