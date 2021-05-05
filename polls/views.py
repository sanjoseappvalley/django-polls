from django.http import HttpResponse


def index(request):
    return HttpResponse(content="Hello, you're at polls index")
