from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TeamViewSet

app_name = "team"

router = DefaultRouter()
router.register("", TeamViewSet, basename="team")


urlpatterns = [
    path("", include(router.urls)),
]
