from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request): 
	return render(request, "diaryIndex.html")

def post(request): 
	return render(request, "diaryIndex.html")


