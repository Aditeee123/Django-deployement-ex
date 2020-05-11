from django.shortcuts import render
# from django
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')
def other(request):
    return render(request,'basic_app/otherpage.html')
def fourth(request):
    return render(request,'basic_app/fourth.html')
def relative_html(request):
    return render(request,'basic_app/relative_page.html')
