from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор регистрации пользователя.
    """

    password = serializers.CharField(
        write_only=True, min_length=8, max_length=32
    )
    username = serializers.CharField(min_length=4, max_length=32)
    email = serializers.EmailField(min_length=6, max_length=64)

    def validate(self, validated_data):
        """
        Валидация уникальности почты
        и юзернейма
        """
        username = validated_data["username"]
        email = validated_data["email"]
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(f"Пользователь {username} уже существует")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(f"Почта {email} уже зарегистрирована")
        return validated_data

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class LogoutSerializer(serializers.Serializer):
    """
    Сериализатор выхода пользователя из системы.
    """

    refresh = serializers.CharField(required=True)  # jWT токен

    @staticmethod
    def validate_refresh(value):
        """
        Верификация refresh токена
        """
        try:
            RefreshToken(value).verify()

        except TokenError:
            raise serializers.ValidationError("Неверный токен")

        return value
    
    def save(self, **kwargs):
        """
        Сохранение данных
        сериализатора и
        отправка токена в черный список.
        """

        RefreshToken(self.validated_data["refresh"]).blacklist()
