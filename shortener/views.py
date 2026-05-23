from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ShortURL, ClickLog
from .utils import create_unique_code


def create_short_url(request):
    if not request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        url = request.POST.get("url")
        code = create_unique_code()

        obj = ShortURL.objects.create(
            user=request.user,
            original_url=url,
            short_code=code
        )

        full_url = request.build_absolute_uri(f"/r/{obj.short_code}/")
        request.session["short_url"] = full_url
        return redirect("create_short_url")

    short_url = request.session.pop("short_url", None)

    return render(request, "shortener/create.html", {
        "short_url": short_url
    })


def redirect_short_url(request, code):
    try:
        short_url = ShortURL.objects.get(short_code=code)
        ip = request.META.get("REMOTE_ADDR")
        user_agent = request.META.get("HTTP_USER_AGENT", "")
        ClickLog.objects.create(
            short_url=short_url,
            ip_address=ip,
            user_agent=user_agent
        )
        return redirect(short_url.original_url)
    except ShortURL.DoesNotExist:
        return HttpResponse("Invalid URL", status=404)
