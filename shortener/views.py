from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL
from .utils import create_unique_code

def home(request):
    print(request.user)
    print(request.user.is_authenticated)
    return HttpResponse(f"Hello, {request.user.username}!")

def create_short_url(request):
    if request.method == "POST":
        url = request.POST.get("url")

        code = create_unique_code()

        obj = ShortURL.objects.create(
            user=request.user,
            original_url=url,
            short_code=code
        )

        return render(request, "shortener/result.html", {
            "short_url": f"/r/{obj.short_code}"
        })

    return render(request, "shortener/create.html")

def redirect_short_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code)
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return HttpResponse("Invalid URL", status=404)
