from rest_framework.response import Response
from rest_framework.views import APIView, status
from rest_framework.permissions import IsAuthenticated

from .serializers import(
    AddCarSerializer,
    AddCommentSerializer,
    AddCountrySerializer,
    AddManufacturerSerializer
)


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
    def post(self,request, *args, **kwargs):
        comment = AddCommentSerializer(data=request.data)
        comment.is_valid(raise_exception=True)
        comment.save()
        return Response(
                {"success": "Комментарий добавлен."},
                status=status.HTTP_201_CREATED,
    )

    