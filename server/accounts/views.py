from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def contact(request):
    return HttpResponse("contact")


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
