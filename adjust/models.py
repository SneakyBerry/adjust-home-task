from django.db import models
from django.utils.translation import gettext_lazy as _


class OperationSystem(models.TextChoices):
    """Choices for operation system."""

    IOS = "ios", _("Apple iOS")
    ANDROID = "android", _("Android OS")


class Adjust(models.Model):
    """Model for home task."""

    date = models.DateField(db_index=True)
    channel = models.TextField(db_index=True)
    country = models.CharField(max_length=2, db_index=True)
    os = models.TextField(choices=OperationSystem.choices, db_index=True)
    impressions = models.PositiveIntegerField(db_index=True)
    clicks = models.PositiveIntegerField(db_index=True)
    installs = models.PositiveIntegerField(db_index=True)
    spend = models.FloatField(db_index=True)
    revenue = models.FloatField(db_index=True)
