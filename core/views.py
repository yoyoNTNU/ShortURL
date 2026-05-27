from django.shortcuts import render

def home(request):
    return render(request, "core/homepage.html")

def private_page(request):
    return render(request, "core/private.html")

def terms_of_service(request):
    return render(request, "core/terms.html")
