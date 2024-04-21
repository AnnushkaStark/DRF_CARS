from django.urls import path

from .views import *

app_name = "main_app"

urlpatterns = [
    path("api/add_country/", AddCountryApiView.as_view(), name="add_country"),
    path("api/add_manufacturer/", AddManufacturerApiView.as_view(), name="add_manufacturer"),
    path("api/car/", AddCarApiView.as_view(), name="add_car"),
    path("api/comment/", AddCommentApiView.as_view(), name="add_comment")
]