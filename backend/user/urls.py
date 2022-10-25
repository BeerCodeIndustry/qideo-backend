from rest_framework import routers
from django.urls import path, include

from .views import AuthUserViewSet


router = routers.SimpleRouter()
router.register(r'user', AuthUserViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]