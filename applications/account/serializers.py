from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from applications.account.utils import send_activation_code

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
        # user.email отправляем на указанный email
        # user.activation_code сгенерированный код
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError('Нет такого пользователя')

    def validate(self, attrs):
        user = authenticate(email=attrs.get('email'), password = attrs.get('password'))
        if not user:
            raise serializers.ValidationError('Неверный пароль')
        attrs['user'] = user
        return attrs


class CreatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, min_length=6 , write_only=True)
    current_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        models = User
        fields =('email', 'password', 'new_password', 'current_password')
