from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import IsAuthenticated

from .serializers import (
    AddCarSerializer,
    AddCommentSerializer,
    AddCountrySerializer,
    AddManufacturerSerializer,
    UpdateCountrySerializer,
    UpdateManufacturerSerializer,
    UpdateCarSerializer,
    UpdateCommentSerializer,
    GetCountrySerializer,
    GetManufacturerSerializer,
    GetCarSerializer,
    GetCommentSerializer,
)
from .models import Car, Comments, Country, Manufacturer


class AddCountryApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        country = AddCountrySerializer(data=request.data)
        country.is_valid(raise_exception=True)
        country.save()
        return Response(
            {"success": "Старна добавлена."},
            status=status.HTTP_201_CREATED,
        )


class AddManufacturerApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        manufacturer = AddManufacturerSerializer(data=request.data)
        manufacturer.is_valid(raise_exception=True)
        manufacturer.save()
        return Response(
            {"success": "Производитель добавлен."},
            status=status.HTTP_201_CREATED,
        )


class AddCarApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        car = AddCarSerializer(data=request.data)
        car.is_valid(raise_exception=True)
        car.save()
        return Response(
            {"success": "Автомобиль добавлен."},
            status=status.HTTP_201_CREATED,
        )


class AddCommentApiView(APIView):

    def post(self, request, *args, **kwargs):
        comment = AddCommentSerializer(data=request.data)
        comment.is_valid(raise_exception=True)
        comment.save()
        return Response(
            {"success": "Комментарий добавлен."},
            status=status.HTTP_201_CREATED,
        )


class DeleteCountryApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            country = Country.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Cтрана не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteManufacturerApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            manufacturer = Manufacturer.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Производитель  не  найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteCarApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Автомобиль  не  найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DeleteСommentApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            comment = Comments.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Комментарий  не  найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateCountryApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            country = Country.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Cтрана не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UpdateCountrySerializer(instance=country)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UpdateManufacturerApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            manufacturer = Manufacturer.objects.get(id=pk)
        except Manufacturer.DoesNotExist:
            return Response(
                {"error": "Производитель не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UpdateManufacturerSerializer(instance=manufacturer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UpdateCarApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Cтрана не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UpdateCarSerializer(instance=car)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UpdateCommentApiView(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        try:
            comment = Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            return Response(
                {"error": "Cтрана не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = UpdateCommentSerializer(instance=comment)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class GetCountryApiView(APIView):
    def get(self, request, pk):
        try:
            country = Country.objects.get(id=pk)
        except Country.DoesNotExist:
            return Response(
                {"error": "Cтрана не  найдена."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetCountrySerializer(instance=country)
        return Response(serializer.data)


class GetManufacturerApiView(APIView):
    def get(self, request, pk):
        try:
            manufacturer = Manufacturer.objects.get(id=pk)
        except Manufacturer.DoesNotExist:
            return Response(
                {"error": "Производитель не найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetCountrySerializer(instance=manufacturer)
        return Response(serializer.data)


class GetManufacturerApiView(APIView):
    def get(self, request, pk):
        try:
            manufacturer = Manufacturer.objects.get(id=pk)
        except Manufacturer.DoesNotExist:
            return Response(
                {"error": "Производитель не найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetManufacturerSerializer(instance=manufacturer)
        return Response(serializer.data)


class GetCarApiView(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
        except Car.DoesNotExist:
            return Response(
                {"error": "Автомобиль не найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetCarSerializer(instance=car)
        return Response(serializer.data)


class GetCommentApiView(APIView):
    def get(self, request, pk):
        try:
            comment = Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            return Response(
                {"error": "Комментнарий не найден."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = GetCommentSerializer(instance=comment)
        return Response(serializer.data)
