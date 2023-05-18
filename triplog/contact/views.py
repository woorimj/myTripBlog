from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostModelForm
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'post_list.html')

def create(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            form.save() 
            return redirect('post_list') 
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts':posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post':post})

def post_update(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')