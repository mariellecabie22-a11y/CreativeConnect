from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreativeProfileForm
from .models import CreativeProfile


def profile_list(request):
    profiles = (
        CreativeProfile.objects
        .filter(available_for_projects=True)
        .select_related("user")
        .order_by("display_name")
    )

    creative_type = request.GET.get("type", "").strip()
    location = request.GET.get("location", "").strip()

    if creative_type:
        profiles = profiles.filter(creative_type=creative_type)

    if location:
        profiles = profiles.filter(location__icontains=location)

    return render(
        request,
        "profiles/profile_list.html",
        {
            "profiles": profiles,
            "creative_types": CreativeProfile.CREATIVE_TYPES,
            "selected_type": creative_type,
            "location_query": location,
        },
    )


def profile_detail(request, username):
    profile = get_object_or_404(
        CreativeProfile.objects.select_related("user"),
        user__username=username,
    )

    return render(
        request,
        "profiles/profile_detail.html",
        {"profile": profile},
    )


@login_required
def profile_create(request):
    if CreativeProfile.objects.filter(user=request.user).exists():
        messages.info(
            request,
            "You already have a profile. You can edit it instead.",
        )
        return redirect("profile-edit")

    if request.method == "POST":
        form = CreativeProfileForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            messages.success(
                request,
                "Your creative profile has been created.",
            )

            return redirect(
                "profile-detail",
                username=request.user.username,
            )
    else:
        form = CreativeProfileForm()

    return render(
        request,
        "profiles/profile_form.html",
        {
            "form": form,
            "title": "Create profile",
            "button_text": "Create profile",
        },
    )


@login_required
def profile_edit(request):
    profile = get_object_or_404(
        CreativeProfile,
        user=request.user,
    )

    if request.method == "POST":
        form = CreativeProfileForm(
            request.POST,
            request.FILES,
            instance=profile,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your profile has been updated.",
            )

            return redirect(
                "profile-detail",
                username=request.user.username,
            )
    else:
        form = CreativeProfileForm(instance=profile)

    return render(
        request,
        "profiles/profile_form.html",
        {
            "form": form,
            "title": "Edit profile",
            "button_text": "Save changes",
            "profile": profile,
        },
    )