from django.shortcuts import render


def index(request):
  return render(request, 'webBlog/index.html')

def band(request):
  return render(request, 'webBlog/band.html')

def tour(request):
  return render(request, 'webBlog/tour.html')

def contact(request):
  return render(request, 'webBlog/contact.html')
