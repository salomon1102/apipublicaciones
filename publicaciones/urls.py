from django.urls import path
from .views import PublicacionViewSet
from rest_framework.routers import DefaultRouter

#path('', Materias.as_view()),


router = DefaultRouter()
router.register(r'', PublicacionViewSet)

urlpatterns = router.urls