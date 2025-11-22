from django.shortcuts import render

# Create your views here.
def home(request):
    d={'author':'Rahim','age':5}
    return render(request,'first_app/home.html',d)
