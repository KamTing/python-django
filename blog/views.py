from django.shortcuts import render
from django.http import HttpResponse


# render 相当于前端渲染器
def index(request):
    return render(request, 'blog/index.html')