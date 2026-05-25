from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_short_url, name="create_short_url"),
    path("r/<str:code>/", views.redirect_short_url),

    path("analytics/", views.total_analytics),
]