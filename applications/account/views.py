from django.contrib.auth import get_user_model , update_session_auth_hash
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from applications.account.serializers import RegisterSerializer

from applications.account.utils import send_activate

# Create your views here.


User = get_user_model()  # работа с юзером


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data) #проверям пароли ,почту
        serializer.is_valid(raise_exception=True)# сверям как он сработал, если все хорошо срабатывает serializer.save
        serializer.save()

        return Response('Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией:', status=201)


class ActivationAPIView(APIView):
    def get(self, request , activation_code):
        user = User.objects.get(activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active', 'activation_code'])
        return Response('Успешно', status=200)

class ChangePasswordAPIView(APIView):
    def post(self, request):
        email = request.data.get('email', '')
        current_password = request.data.get('current_password', '')
        new_password = request.data.get('new_password', '')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response('Пользователь с такой почтой не найден', status=status.HTTP_400_BAD_REQUEST)
        if not user.check_password(current_password):
            return Response('Неверный текущий пароль', status=status.HTTP_400_BAD_REQUEST)
        if len(new_password) < 6:
            return Response('Новый пароль должен содержать не менее 6 символов', status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        send_activate(user.email, user.activation_code)
        send_mail(
            'Уведомление о смене пароля',
            'Ваш пароль был успешно изменен.',
            'RodionDereha@gmail.com',
            [email],
            fail_silently=False,
        )

        update_session_auth_hash(request, user)
        return Response('Пароль успешно изменен', status=status.HTTP_200_OK)
