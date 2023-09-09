from django.contrib.auth import get_user_model
from rest_framework import serializers

from account.utils import send_activation_code

User = get_user_model() #получаем модельки юзера


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, required=True, write_only=True)
    """
    RegisterSerializer - создаем 2 пароль для регистрации в дальнейшем будем сравнивать его с 1 
    """

    class Meta:
        model = User  # Будем работать с User , из models
        fields = ('email', 'password', 'password2')

    def validate_email(self, email):
        return email

    def validate(self, attrs):
        # получам 1 пароль при помощи get()
        p1 = attrs.get('password')
        # получаем 2 пароль и удаляем его для эффективности при помощи pop()
        p2 = attrs.pop('password2')
        # сравниваем пароли
        if p1 != p2:
            raise serializers.ValidationError('Убедитесь что пароли схожи')
        return attrs

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        send_activation_code(user.email, user.activation_code)
        # user.email отправляем на казанный email
        # user.activation_code сгенерированный код
        return user