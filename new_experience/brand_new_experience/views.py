from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import reviewerRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')


def loginPortal(request):
    pass 


def reviewerSignUp(request):
    form = reviewerRegisterForm()
    
    if (request.method == 'POST'):
        form = reviewerRegisterForm(request.POST)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_reviewer = True 
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('reviewerHome')
        else:
            form = reviewerRegisterForm()
    return render(request, 'reviewerSignup.html', {'form': form})



def bloggerSignUp(request):
    pass

@login_required
def reviewerHome(request):
    return render(request, 'reviewerHome.html')

def reviewerLogin(request):
    pass 

def logoutUser(request):
    logout(request)
    return redirect('home')