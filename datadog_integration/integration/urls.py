from django.urls import path

from datadog_integration.integration.views import (
    datadog_alert, validate_api_key, mute_monitor, resolve_monitor, list_all_monitor
)

from datadog_integration.integration.api.views import (
    CreateAuthenticationKeyAPIView, ListAlertAPIView,
    ListAuthenticationKeyAPIView, DestroyAuthenticationKeyAPIView
)


app_name = "integration"
urlpatterns = [
    path("alert/", view=datadog_alert, name="alert"),
    path("auth-key/", view=CreateAuthenticationKeyAPIView.as_view(), name="auth-key"),
    path("validate-key/", view=validate_api_key, name="validate-key"),
    path("list-alerts/", view=ListAlertAPIView.as_view(), name="list-alerts"),
    path("list-keys/", view=ListAuthenticationKeyAPIView.as_view(), name="list-keys"),
    path("destroy-key/<int:pk>/", view=DestroyAuthenticationKeyAPIView.as_view(), name="destroy-keys"),
    path("mute-monitor/<str:monitor_id>/", view=mute_monitor, name="mute-monitor"),
    path("resolve-monitor/<str:monitor_id>/<str:group>/", view=resolve_monitor, name="resolve-monitor"),
    path("list-monitor/", view=list_all_monitor, name="list-monitor"),
]