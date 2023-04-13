from django.shortcuts import render, redirect
from .models import WriteModel
from django.contrib.auth.decorators import login_required


def main(request):
    user = request.user.is_authenticated
    if user:
        return redirect("/main-page")
    else:
        return redirect("/sign-in")


@login_required
def main_page_view(request):
    if request.method == "GET":  # 요청하는 방식이 GET 방식인지 확인하기
        user = request.user.is_authenticated  # 사용자가 로그인이 되어 있는지 확인하기
        if user:  # 로그인 한 사용자라면
            all_write = WriteModel.objects.all().order_by("-created_at")
            return render(request, "write_page/main.html", {"writes": all_write})
        else:  # 로그인이 되어 있지 않다면
            return redirect("/sign-in")


@login_required
def write_page_view(request):
    return render(request, "write_page/write.html")
    # elif request.method == 'POST':  # 요청 방식이 POST 일때
    # user = request.user  # 현재 로그인 한 사용자를 불러오기
    # my_page = PageModel()  # 글쓰기 모델 가져오기
    # my_page.author = user  # 모델에 사용자 저장
    # my_page.content = request.POST.get('my-content', '')  # 모델에 글 저장
    # my_page.save()
    # return redirect('/main')


@login_required
def write_page_create(request):
    if request.method == "POST":
        # my_writings = WriteModel()
        user = request.user
        title = request.POST["title"]
        content = request.POST["content"]
        WriteModel.objects.create(
            author=user,
            title=title,
            content=content,
        )
        return redirect("/main-page")
        # redirect("/main-page")
