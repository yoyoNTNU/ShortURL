import string
import random
from .models import ShortURL
from django.http import HttpResponse

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_unique_code():
    while True:
        code = generate_code()
        if not ShortURL.objects.filter(short_code=code).exists():
            return code

def denied_unauthorized(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized", status=401)
    return None

def denied_forbidden(request, auth_user):
    if request.user != auth_user:
        return HttpResponse("Forbidden", status=403)
    return None
