from django.urls import path

# from charts.views import index, yahoo, view_chart, iexcloud
from apps.charts.views import homeView, cryptoView, index

urlpatterns = [
    path('', index, name='index'),
    # path('yahoo/', yahoo, name='yahoo'),
    # path('view/', view_chart, name='view_chart'),
    # path('iex/', iexcloud, name='iexcloud'),
    path('home/', homeView, name="home"),
    path('crypto/', cryptoView, name="crypto"),
]
