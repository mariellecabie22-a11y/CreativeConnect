from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.inbox,
        name="inbox",
    ),
    path(
        "sent/",
        views.sent_messages,
        name="sent-messages",
    ),
    path(
        "new/",
        views.message_create,
        name="message-create",
    ),
    path(
        "new/<str:username>/",
        views.message_create,
        name="message-create-to-user",
    ),
    path(
        "conversation/<str:username>/",
        views.conversation,
        name="conversation",
    ),
    path(
        "<int:pk>/",
        views.message_detail,
        name="message-detail",
    ),
    path(
        "<int:pk>/reply/",
        views.message_reply,
        name="message-reply",
    ),
]