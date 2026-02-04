from django.urls import path
from .views import home, pricing

urlpatterns = [
    path('', home, name='homepage'),
    path('pricing', pricing, name='pricing'),
]
