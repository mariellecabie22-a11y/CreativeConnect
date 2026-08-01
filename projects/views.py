from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectForm
from .models import Project


def project_list(request):
    projects = (
        Project.objects
        .select_related("owner")
        .order_by("-created_at")
    )

    category = request.GET.get("category", "").strip()
    location = request.GET.get("location", "").strip()
    status = request.GET.get("status", "").strip()

    if category:
        projects = projects.filter(category__icontains=category)

    if location:
        projects = projects.filter(location__icontains=location)

    if status:
        projects = projects.filter(status=status)

    return render(
        request,
        "projects/project_list.html",
        {
            "projects": projects,
            "category_query": category,
            "location_query": location,
            "selected_status": status,
            "status_choices": Project.STATUS_CHOICES,
        },
    )


def project_detail(request, pk):
    project = get_object_or_404(
        Project.objects.select_related("owner"),
        pk=pk,
    )

    return render(
        request,
        "projects/project_detail.html",
        {"project": project},
    )


@login_required
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            messages.success(
                request,
                "Your project has been created.",
            )

            return redirect(
                "project-detail",
                pk=project.pk,
            )
    else:
        form = ProjectForm()

    return render(
        request,
        "projects/project_form.html",
        {
            "form": form,
            "title": "Create project",
            "button_text": "Create project",
        },
    )


@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.owner != request.user:
        return HttpResponseForbidden(
            "You cannot edit another user's project."
        )

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            instance=project,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your project has been updated.",
            )

            return redirect(
                "project-detail",
                pk=project.pk,
            )
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "projects/project_form.html",
        {
            "form": form,
            "title": "Edit project",
            "button_text": "Save changes",
            "project": project,
        },
    )


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if project.owner != request.user:
        return HttpResponseForbidden(
            "You cannot delete another user's project."
        )

    if request.method == "POST":
        project.delete()

        messages.success(
            request,
            "Your project has been deleted.",
        )

        return redirect("project-list")

    return render(
        request,
        "projects/project_confirm_delete.html",
        {"project": project},
    )