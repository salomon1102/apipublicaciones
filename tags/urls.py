from django.urls import path
from .views import TagViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', TagViewSet)

urlpatterns = router.urls