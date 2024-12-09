from django.shortcuts import render
from . import views
from django.http import HttpResponse
from .models import Comment

# Create your views here.
# def home(request):
#   return HttpResponse('welcome home')

def comments(request):
  comm=Comment.objects.all()
  return render(request,'comment.html',{'comm':comm})