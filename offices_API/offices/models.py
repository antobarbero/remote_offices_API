from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class OfficeFeature(models.Model):
    """Is a feature of an office."""
    title = models.CharField(max_length=100)


class InternetSpeedTest(models.Model):
    """Represents an executed connection test."""
    date_time = models.DateTimeField(default=timezone.now)
    download_speed = models.DecimalField(max_digits=6, decimal_places=2)
    upload_speed = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.URLField(null=True, blank=True)


class Office(models.Model):
    """Represents a working office."""

    adsl, satellite, i3g, i4g, i5g, air = range(6)

    CONNECTION_TYPE_CHOICES = (
        (adsl, 'ADSL'),
        (satellite, 'Satellite'),
        (i3g, '3G'),
        (i4g, '4G'),
        (i5g, '5G'),
        (air, 'Air'),
    )

    title = models.CharField(max_length=200)
    summary = models.TextField()
    #  TODO pass this to PointField
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    features = models.ManyToManyField(OfficeFeature, related_name='offices')
    internet_speed_tests = models.ManyToManyField(
        InternetSpeedTest,
        related_name='offices'
    )
    internet_connection_type = models.SmallIntegerField(
        choices=CONNECTION_TYPE_CHOICES
    )


class OfficeImage(models.Model):
    """Is a photo of an office."""
    office = models.ForeignKey(
        Office,
        on_delete=models.PROTECT,
        related_name='images'
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='media')
