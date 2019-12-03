from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')
def login(request):
    return render(request,'pages/login.html')
def Add_user(request):
    return render(request,'pages/register_user.html')
def Dash_board(request):
    return render(request,'pages/dashboard.html')
def user_profile(request):
    return render(request,'dashboard/user_profile.html')
def map(request):
    return render(request,'dashboard/map.html')