from django.http import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Article
from .serializers import ArticleSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def contact(request):
    return HttpResponse("contact")


def home(request):
    return HttpResponse("home")


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
