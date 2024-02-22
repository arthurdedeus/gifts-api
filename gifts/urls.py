from django.urls import include, path
from rest_framework import routers

from gifts import views

app_name = "gifts"

router = routers.SimpleRouter()
router.register(r"gifts", views.GiftViewSet, basename="gifts")

urlpatterns = [path(r"", include(router.urls))]
