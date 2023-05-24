from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostModelForm
from .models import Post

def home(request): 
	return render(request, "diary_list.html")

def post(request): 
	return render(request, "diaryIndex.html")

def create(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            form.save() 
            return redirect('diary_list') 
    else:
        form = PostModelForm() 
    return render(request, 'diary_form_create.html', {'form':form})

def diary_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'diary_list.html', {'posts':posts})
