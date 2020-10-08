from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from datadog_integration.users.api.views import UserViewSet
from datadog_integration.integration.api.views import CreateAuthenticationKeyAPIView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
# router.register("auth-key", CreateAuthenticationKeyAPIView)


app_name = "api"
urlpatterns = router.urls
