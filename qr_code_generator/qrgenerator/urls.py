from django.urls import path
from .views import generate_qr_code, display_qr_code

urlpatterns = [
    path("generate/", generate_qr_code, name="generate_qr_code"),
    path("display/", display_qr_code, name="display_qr_code"),
]