from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import PostModelForm
from .models import Post

def home(request): 
	return render(request, "diary_list.html")

def post(request): 
	return render(request, "diaryIndex.html")

def diary_create(request):
    if request.method == 'POST' or request.method == "FILES":
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST, request.FILES)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save() 
            return redirect('diary_list') 
    else:
        form = PostModelForm() 
    return render(request, 'diary_form_create.html', {'form':form})

def diary_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'diary_list.html', {'posts':posts})

def diary_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    #comment_form = CommentForm()
    context={
        'post':post,
        #'comment_form' : comment_form
    }
    return render(request, 'diary_detail.html', context)

def diary_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'diary_form_create.html', {'form':form, 'id':id})

def diary_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('diary_list')