from django.urls import path

from auth.views import UserCreateView

app_name = "auth"


urlpatterns = [
    path("users/", UserCreateView.as_view(), name="user-create"),
]
