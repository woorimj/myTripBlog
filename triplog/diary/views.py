from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request): 
	return render(request, "diaryHome.html")

def post(request): 
	return render(request, "post.html")


