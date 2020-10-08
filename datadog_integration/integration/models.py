from django.db import models


class DatadogAlert(models.Model):
    """Model definition for DatadogAlert."""

    payload = models.JSONField()
    class Meta:
        """Meta definition for DatadogAlert."""

        verbose_name = 'datadog_alert'
        verbose_name_plural = 'MODdatadog_alerts'

    def __str__(self):
        """Unicode representation of DatadogAlert."""
        pass


class AuthenticationKey(models.Model):
    """Model definition fo AuthenticationKey."""
    API_KEY = 'API_KEY'
    APPLICATION_KEY = 'APP_KEY'
    KEY_TYPE_CHOICES = [
        (API_KEY, 'API Key'),
        (APPLICATION_KEY, 'Application Key'),
    ]

    name = models.CharField(max_length=150 ,null=True, blank=True)
    key = models.CharField(max_length=150)
    key_type = models.CharField(max_length=25, choices=KEY_TYPE_CHOICES)


    class Meta:
        """Meta definition for AuthenticationKey."""

        verbose_name = 'authentication_key'
        verbose_name_plural = 'authentication_keys'

    def __str__(self):
        """Unicode representation of AuthenticationKey."""
        return self.name


