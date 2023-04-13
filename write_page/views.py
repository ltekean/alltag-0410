from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def see_detail_page(request, user_id):
    pages = Page.objects.all()
    return render(
        request,
        "detail_page.html",
        {"pages": pages},
    )
