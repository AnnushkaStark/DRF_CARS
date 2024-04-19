from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer, LogoutSerializer



class RegisterApiView(APIView):
    """
    Представление регистрации пользователя
    Входные данные: username, email, password
    """
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"success": "Пользователь успешно создан"},
            status=status.HTTP_201_CREATED,
        )


class LogoutApiView(APIView):
    """
    Представление выходя пользователя из системы
    """
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        black_token = LogoutSerializer(data=request.data)
        black_token.is_valid(raise_exception=True)
        black_token.save()
        return Response(
            {"success": "Вы успешно вышли из аккаунта."},
            status=status.HTTP_200_OK,
    )


class TokenObtainPairView(TokenObtainPairView):
    """
    Переопределение представления TokenObtainPairView
    из библиотеки simple jwt
    """
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class TokenRefreshView(TokenRefreshView):
    """
    Переопределения представления TokenRefreshView
    из библиотеки simple jwt
    """
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
