from django.urls import path
from rest_framework import routers

from .views import VitalDataViewSet

router = routers.DefaultRouter()
router.register("vitaldata", VitalDataViewSet, "user")

urlpatterns = router.urls
