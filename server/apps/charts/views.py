from django.shortcuts import render, get_object_or_404

def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})
