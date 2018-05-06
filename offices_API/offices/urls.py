from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views import OfficeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'offices', OfficeViewSet, base_name='offices')

app_name = 'offices'

urlpatterns = [
    url(
        r'^api/',
        include(router.urls),
    )
]
