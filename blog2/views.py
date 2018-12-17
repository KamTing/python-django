from django.shortcuts import render


# render 相当于前端渲染器
def index(request):
    return render(request, 'blog2/index.html')
