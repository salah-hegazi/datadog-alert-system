from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from .serializers import AuthenticationKeySerializer, AlertSerializer
from ..models import AuthenticationKey, DatadogAlert


class CreateAuthenticationKeyAPIView(CreateAPIView):
    serializer_class = AuthenticationKeySerializer


class ListAlertAPIView(ListAPIView):
    serializer_class = AlertSerializer
    queryset = DatadogAlert.objects.all()


class ListAuthenticationKeyAPIView(ListAPIView):
    serializer_class = AuthenticationKeySerializer
    queryset = AuthenticationKey.objects.all()


class DestroyAuthenticationKeyAPIView(DestroyAPIView):
    serializer_class = AuthenticationKeySerializer
    
    def get_queryset(self):
        queryset = AuthenticationKey.objects.filter(id=self.kwargs['pk'])
        return queryset
