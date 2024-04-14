from django.urls import include, path
from rest_framework import routers

from gifts import views

app_name = "gifts"

router = routers.SimpleRouter()
router.register(r"gifts", views.GiftViewSet, basename="gifts")
router.register(r"checkouts", views.CheckoutViewSet, basename="checkouts")

urlpatterns = [path(r"", include(router.urls))]
