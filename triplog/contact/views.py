from django.shortcuts import redirect, render
from .forms import PostModelForm

# Create your views here.
def home(request):
    return render(request, 'diaryHome.html')

def create(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = PostModelForm(request.POST)
        # 제대로 입력되었는지 검사하는 코드
        if form.is_valid(): 
            # 유효하다면 저장하는 코드
            form.save() 
            return redirect('home') 
    else:
        form = PostModelForm() 
    return render(request, 'form_create.html', {'form':form})
