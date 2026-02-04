# core/models.py
from django.db import models


# Create your models here.
class InternetPlan(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    speed_mbps = models.IntegerField()
    base_price = models.IntegerField(help_text="Monthly price without rental")
    rental_price = models.IntegerField(default=0)

    cta = models.CharField(max_length=50, default="Get Started")

    features = models.ManyToManyField("Feature", blank=True)

    def all_features(self):
        global_features = Feature.objects.filter(is_global=True)
        return global_features | self.features.all()


class Feature(models.Model):
    text = models.CharField(max_length=255)
    is_global = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text
