# core/admin.py
from django.contrib import admin
from .models import InternetPlan, Feature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("text", "is_global", "order")
    list_filter = ("is_global",)
    ordering = ("order",)


@admin.register(InternetPlan)
class InternetPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "speed_mbps", "base_price")
    filter_horizontal = ("features",)
