import string
import random
from .models import ShortURL

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def create_unique_code():
    while True:
        code = generate_code()
        if not ShortURL.objects.filter(short_code=code).exists():
            return code