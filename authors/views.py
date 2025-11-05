from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# Create your views here.
def test(request: WSGIRequest):
    return render(request, 'test.html')
