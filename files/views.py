from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello there")

def files(request):
    return render(request, "files/files.html", {"files": "test-data"})