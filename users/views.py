from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect("/")
        else:
            return render(request, "user/signup.html")
    elif request.method == "POST":
        username = request.POST.get("username", "")
        nickname = request.POST.get("nickname", "")
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if password != password2:
            return render(request, "user/signup.html", {"error": "password를 확인 해 주세요!"})
        else:
            if username == "" or password == "" or nickname =="":
                return render(
                    request, "user/signup.html", {"error": "사용자 이름과 비밀번호, 닉네임은 필수로 입력 해 주세요."}
                )

            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다.'})  # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
            else:
                UserModel.objects.create_user(username=username,password=password,nickname=nickname)
                return redirect("/sign-in")


def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect("/")
        else:
            return render(request, "user/signin.html", {"error": "유저이름 또는 패스워드를 확인하세요"})
    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return redirect("/")
        else:
            return render(request, "user/signin.html")


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/")



@login_required
def my_page(request,user_id):
    users = UserModel.objects.get(id=user_id)
    if request.method == 'POST':
        users.image = request.FILES.get('image')
        users.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    else:
        return render(request, 'user/mypage.html')
            

@login_required
def profile_img_delete(request, user_id):
    users = UserModel.objects.get(id=user_id)
    if users.id == request.user.id:
        users.image.delete()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return redirect("/")

@login_required
def change_nickname(request, user_id):
    users = UserModel.objects.get(id=user_id)
    if request.method == 'POST':
        users.nickname = request.POST.get('nickname')
        users.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    return render('/')
    