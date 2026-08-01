from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User

from .forms import MessageForm
from .models import Message


@login_required
def inbox(request):
    received_messages = (
        Message.objects
        .filter(receiver=request.user)
        .select_related("sender")
        .order_by("-created_at")
    )

    return render(
        request,
        "messaging/inbox.html",
        {
            "received_messages": received_messages,
        },
    )


@login_required
def sent_messages(request):
    messages_sent = (
        Message.objects
        .filter(sender=request.user)
        .select_related("receiver")
        .order_by("-created_at")
    )

    return render(
        request,
        "messaging/sent_messages.html",
        {
            "messages_sent": messages_sent,
        },
    )


@login_required
def message_detail(request, pk):
    message = get_object_or_404(
        Message.objects.select_related(
            "sender",
            "receiver",
        ),
        pk=pk,
    )

    if (
        request.user != message.sender
        and request.user != message.receiver
    ):
        return HttpResponseForbidden(
            "You cannot view this message."
        )

    if request.user == message.receiver and not message.is_read:
        message.is_read = True
        message.save(update_fields=["is_read"])

    return render(
        request,
        "messaging/message_detail.html",
        {
            "message_object": message,
        },
    )


@login_required
def message_create(request, username=None):
    initial_data = {}

    if username:
        receiver = get_object_or_404(
            User,
            username=username,
        )

        if receiver == request.user:
            messages.error(
                request,
                "You cannot send a message to yourself.",
            )
            return redirect("inbox")

        initial_data["receiver"] = receiver

    if request.method == "POST":
        form = MessageForm(
            request.POST,
            sender=request.user,
        )

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user

            if message.receiver == request.user:
                form.add_error(
                    "receiver",
                    "You cannot send a message to yourself.",
                )
            else:
                message.save()

                messages.success(
                    request,
                    "Your message has been sent.",
                )

                return redirect(
                    "message-detail",
                    pk=message.pk,
                )
    else:
        form = MessageForm(
            sender=request.user,
            initial=initial_data,
        )

    return render(
        request,
        "messaging/message_form.html",
        {
            "form": form,
            "title": "New message",
            "button_text": "Send message",
        },
    )


@login_required
def message_reply(request, pk):
    original_message = get_object_or_404(
        Message.objects.select_related(
            "sender",
            "receiver",
        ),
        pk=pk,
    )

    if (
        request.user != original_message.sender
        and request.user != original_message.receiver
    ):
        return HttpResponseForbidden(
            "You cannot reply to this message."
        )

    if request.user == original_message.sender:
        receiver = original_message.receiver
    else:
        receiver = original_message.sender

    subject = original_message.subject

    if not subject.lower().startswith("re:"):
        subject = f"Re: {subject}"

    initial_data = {
        "receiver": receiver,
        "subject": subject,
    }

    if request.method == "POST":
        form = MessageForm(
            request.POST,
            sender=request.user,
        )

        if form.is_valid():
            reply = form.save(commit=False)
            reply.sender = request.user

            if reply.receiver != receiver:
                form.add_error(
                    "receiver",
                    "The reply recipient cannot be changed.",
                )
            else:
                reply.save()

                messages.success(
                    request,
                    "Your reply has been sent.",
                )

                return redirect(
                    "message-detail",
                    pk=reply.pk,
                )
    else:
        form = MessageForm(
            sender=request.user,
            initial=initial_data,
        )

        form.fields["receiver"].disabled = True

    return render(
        request,
        "messaging/message_form.html",
        {
            "form": form,
            "title": "Reply to message",
            "button_text": "Send reply",
            "original_message": original_message,
        },
    )


@login_required
def conversation(request, username):
    other_user = get_object_or_404(
        User,
        username=username,
    )

    if other_user == request.user:
        messages.error(
            request,
            "You cannot open a conversation with yourself.",
        )
        return redirect("inbox")

    conversation_messages = (
        Message.objects
        .filter(
            Q(sender=request.user, receiver=other_user)
            | Q(sender=other_user, receiver=request.user)
        )
        .select_related("sender", "receiver")
        .order_by("created_at")
    )

    Message.objects.filter(
        sender=other_user,
        receiver=request.user,
        is_read=False,
    ).update(is_read=True)

    return render(
        request,
        "messaging/conversation.html",
        {
            "other_user": other_user,
            "conversation_messages": conversation_messages,
        },
    )