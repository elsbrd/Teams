from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, PersonViewSet

app_name = 'teammanagement'

router = DefaultRouter()
router.register(r"teams", TeamViewSet, basename='teams')
router.register(r"people", PersonViewSet, basename='people')

urlpatterns = [
    path("", include(router.urls)),
]
