from django.urls import path
from apps.charts.views import (
    about
)


app_name = "charts"


urlpatterns = [
    path('', about, name='about'),
]
