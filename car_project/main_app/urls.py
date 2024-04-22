from django.urls import path

from .views import *

app_name = "main_app"

urlpatterns = [
    path("api/add_country/", AddCountryApiView.as_view(), name="add_country"),
    path(
        "api/add_manufacturer/",
        AddManufacturerApiView.as_view(),
        name="add_manufacturer",
    ),
    path("api/add_car/", AddCarApiView.as_view(), name="add_car"),
    path("api/add_comment/", AddCommentApiView.as_view(), name="add_comment"),
    path(
        "api/delete_country/<int:pk>/",
        DeleteCountryApiView.as_view(),
        name="delete_county",
    ),
    path(
        "api/delete_manufacturer/<int:pk>/",
        DeleteManufacturerApiView.as_view(),
        name="delete_manufacturer",
    ),
    path("api/delete_car/<int:pk>/", DeleteCarApiView.as_view(), name="delete_car"),
    path(
        "api/delete_comment/<int:pk>/",
        DeleteСommentApiView.as_view(),
        name="delete_comment",
    ),
    path(
        "api/update_country/<int:pk>/",
        UpdateCountryApiView.as_view(),
        name="update_country",
    ),
    path(
        "api/update_manufacturer/<int:pk>/",
        UpdateManufacturerApiView.as_view(),
        name="update_manufacturer",
    ),
    path("api/update_car/<int:pk>/", UpdateCarApiView.as_view(), name="update_car"),
    path(
        "api/update_comment/<int:pk>/",
        UpdateCommentApiView.as_view(),
        name="update_comment",
    ),
    path("api/get_country/<int:pk>/", GetCountryApiView.as_view(), name="get_country"),
    path(
        "api/get_manufacturer/<int:pk>/",
        GetManufacturerApiView.as_view(),
        name="get_manufacturer",
    ),
    path("api/get_car/<int:pk>/", GetCarApiView.as_view(), name="get_car"),
    path("api/get_comment/<int:pk>/", GetCommentApiView.as_view(), name="get_comment"),
]
