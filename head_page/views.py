from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import headModel


# Create your views here.
# @login_required
def Page(request):
    if request.method == "GET":  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_page = headModel.objects.all().order_by("-created_at")
            return render(request, "head_page/main.html", {"page": all_page})
        else:  # 로그인이 되어 있지 않다면
            return redirect("/sign-in")
    # elif request.method == 'POST':  # 요청 방식이 POST 일때
    # user = request.user  # 현재 로그인 한 사용자를 불러오기
    # my_page = PageModel()  # 글쓰기 모델 가져오기
    # my_page.author = user  # 모델에 사용자 저장
    # my_page.content = request.POST.get('my-content', '')  # 모델에 글 저장
    # my_page.save()
    # return redirect('/main')
