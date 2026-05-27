from django.db import models
from django.contrib.auth.models import User

class ShortURL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ClickLog(models.Model):
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    user_browser = models.CharField(max_length=50, blank=True)
    user_os = models.CharField(max_length=50, blank=True)
    user_device = models.CharField(max_length=20, blank=True)
    clicked_at = models.DateTimeField(auto_now_add=True)