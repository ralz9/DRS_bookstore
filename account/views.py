from django.contrib.auth import get_user_model
from django.shortcuts import render , get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import RegisterSerializer

# Create your views here.


User = get_user_model()  # работа с юзером


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) #проверям пароли ,почту
        serializer.is_valid(raise_exception=True)# сверям как он сработал, если все хорошо срабатывает serializer.save
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией:', status=201)


class ActivationAPIView(APIView):
    def post(self, request , activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_activ', 'activation_code'])
        return Response('Успешно', status=200)
