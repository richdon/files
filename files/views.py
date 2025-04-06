from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import UploadForm
from .models import File


def _get_file(file_id):
    try:
        return File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return redirect("files")


def home(request):
    return HttpResponse("Hello there")


def files(request):
    data = File.objects.all()
    return render(request, "files/files.html", {"files": data, "form": UploadForm})


def file(request, file_id):
    f = _get_file(file_id)
    # If _get_file returned a redirect
    if hasattr(f, 'status_code'):
        return f
    return render(request, "files/file.html", {"file": f})  # Changed "files" to "file"


def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect("files")


def edit(request, file_id):
    f = _get_file(file_id)
    # If _get_file returned a redirect
    if hasattr(f, 'status_code'):
        return f

    if name := request.POST.get("name"):
        f.name = name
    if file_type := request.POST.get("file_type"):
        f.file_type = file_type
    f.save()
    return redirect("files")  # Added return and changed to URL name


def delete(request, file_id):
    f = _get_file(file_id)
    # If _get_file returned a redirect
    if hasattr(f, 'status_code'):
        return f

    f.delete()
    return redirect("files")  # Added return and changed to URL name
