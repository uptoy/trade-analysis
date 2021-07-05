from django.urls import path
from apps.charts.views import HomeView,CryptoView


app_name = "charts"

urlpatterns = [
    path('home/', HomeView, name="home"),
    path('crypto/', CryptoView, name="crypto"),

]
