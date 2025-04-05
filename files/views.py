from django.http import HttpResponse, Http404
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello there")


data = [
    {
        "id": 0,
        "name": "image1.jpeg",
        "type": "jpeg"
    },
    {
        "id": 1,
        "name": "notes.txt",
        "type": "txt"
    },
    {
        "id": 2,
        "name": "image2.jpeg",
        "type": "jpeg"
    }
]


def files(request):
    return render(request, "files/files.html", {"files": data})


def file(request, file_id):
    if not (f := next((item for item in data if item["id"] == file_id), None)):
        raise Http404("file does not exist")
    return render(request, "files/file.html", {"files": f})
