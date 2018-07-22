from django.shortcuts import render,redirect
from Booktest.models import BookInfo
from django.http import JsonResponse,HttpResponse
from datetime import date
# Create your views here.


def index(request):
    books=BookInfo.objects.all()
    return render(request,"Booktest/index.html",{"books":books})


def create(request):
    b=BookInfo()
    b.btitle="鹿鼎记"
    b.bpub_date=date(1999,1,1)
    b.save()
    return redirect("/index")

def delete(request,bid):
    book=BookInfo.objects.get(id=bid)
    book.delete()
    return redirect("/index")


def detail(request,bid):
    book=BookInfo.objects.get(id=bid)
    heros=book.heroinfo_set.all()
    return render(request,"Booktest/detail.html",{"heros":heros,"book":book})



def login(request):
    username=request.GET.get("username")
    password=request.GET.get("password")
    if username=="123" and password=="123":
        return JsonResponse({'ret':1})
    else:
        return JsonResponse({'ret':0})
