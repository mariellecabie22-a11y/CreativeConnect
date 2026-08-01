from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.profile_list,
        name="profile-list",
    ),
    path(
        "create/",
        views.profile_create,
        name="profile-create",
    ),
    path(
        "edit/",
        views.profile_edit,
        name="profile-edit",
    ),
    path(
        "<str:username>/",
        views.profile_detail,
        name="profile-detail",
    ),
]