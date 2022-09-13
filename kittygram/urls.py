from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet

router = DefaultRouter()
router.register('api/v1/cats', CatViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
