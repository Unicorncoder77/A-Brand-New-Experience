from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')


def loginPortal(request):
    pass 


def reviewerSignUp(request):
    return render(request, 'reviewerSignup.html') 

def bloggerSignUp(request):
    pass

@login_required
def reviewerHome(request):
    pass 

def reviewerLogin(request):
    pass 

