from django.urls import path

from . import views


urlpatterns = [
    path(
        "mine/",
        views.my_applications,
        name="my-applications",
    ),
    path(
        "apply/<int:project_pk>/",
        views.application_create,
        name="application-create",
    ),
    path(
        "<int:pk>/",
        views.application_detail,
        name="application-detail",
    ),
    path(
        "<int:pk>/withdraw/",
        views.application_withdraw,
        name="application-withdraw",
    ),
    path(
        "<int:pk>/status/<str:status>/",
        views.application_update_status,
        name="application-update-status",
    ),
    path(
        "project/<int:project_pk>/",
        views.project_applications,
        name="project-applications",
    ),
]