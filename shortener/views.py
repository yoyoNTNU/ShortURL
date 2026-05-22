from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print(request.user)
    print(request.user.is_authenticated)
    return HttpResponse(f"Hello, {request.user.username}!")
