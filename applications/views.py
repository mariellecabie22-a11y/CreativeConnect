from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from projects.models import Project

from .forms import ApplicationForm
from .models import Application


@login_required
def application_create(request, project_pk):
    project = get_object_or_404(
        Project,
        pk=project_pk,
        status="open",
    )

    if project.owner == request.user:
        messages.error(
            request,
            "You cannot apply to your own project.",
        )
        return redirect(
            "project-detail",
            pk=project.pk,
        )

    existing_application = Application.objects.filter(
        project=project,
        applicant=request.user,
    ).first()

    if existing_application:
        messages.warning(
            request,
            "You have already applied to this project.",
        )
        return redirect(
            "application-detail",
            pk=existing_application.pk,
        )

    if request.method == "POST":
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.project = project
            application.applicant = request.user
            application.save()

            messages.success(
                request,
                "Your application has been submitted.",
            )

            return redirect(
                "application-detail",
                pk=application.pk,
            )
    else:
        form = ApplicationForm()

    return render(
        request,
        "applications/application_form.html",
        {
            "form": form,
            "project": project,
        },
    )


@login_required
def application_detail(request, pk):
    application = get_object_or_404(
        Application.objects.select_related(
            "project",
            "applicant",
            "project__owner",
        ),
        pk=pk,
    )

    if (
        request.user != application.applicant
        and request.user != application.project.owner
    ):
        return HttpResponseForbidden(
            "You cannot view this application."
        )

    return render(
        request,
        "applications/application_detail.html",
        {"application": application},
    )


@login_required
def my_applications(request):
    applications = (
        Application.objects
        .filter(applicant=request.user)
        .select_related("project", "project__owner")
        .order_by("-created_at")
    )

    return render(
        request,
        "applications/my_applications.html",
        {"applications": applications},
    )


@login_required
def project_applications(request, project_pk):
    project = get_object_or_404(
        Project,
        pk=project_pk,
    )

    if project.owner != request.user:
        return HttpResponseForbidden(
            "Only the project owner can view applications."
        )

    applications = (
        project.applications
        .select_related("applicant")
        .order_by("-created_at")
    )

    return render(
        request,
        "applications/project_applications.html",
        {
            "project": project,
            "applications": applications,
        },
    )


@login_required
def application_update_status(request, pk, status):
    application = get_object_or_404(
        Application.objects.select_related("project"),
        pk=pk,
    )

    if application.project.owner != request.user:
        return HttpResponseForbidden(
            "Only the project owner can update applications."
        )

    allowed_statuses = {"accepted", "rejected"}

    if request.method != "POST":
        return redirect(
            "project-applications",
            project_pk=application.project.pk,
        )

    if status not in allowed_statuses:
        messages.error(
            request,
            "Invalid application status.",
        )
    else:
        application.status = status
        application.save(update_fields=["status"])

        messages.success(
            request,
            f"Application marked as {status}.",
        )

    return redirect(
        "project-applications",
        project_pk=application.project.pk,
    )


@login_required
def application_withdraw(request, pk):
    application = get_object_or_404(
        Application,
        pk=pk,
        applicant=request.user,
    )

    if request.method == "POST":
        application.delete()

        messages.success(
            request,
            "Your application has been withdrawn.",
        )

        return redirect("my-applications")

    return render(
        request,
        "applications/application_confirm_withdraw.html",
        {"application": application},
    )