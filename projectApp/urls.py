from django.urls import path
from .views import RegistrationView,LoginView
# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )
# from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
]