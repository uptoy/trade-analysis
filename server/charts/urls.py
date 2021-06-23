from django.urls import path, include

from .views import ArticleListView, ArticleDetailView, index, home, contact

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('contact/', contact, name='contact'),
    path('list/', ArticleListView.as_view()),
    path('list/<pk>/', ArticleDetailView.as_view()),

]
