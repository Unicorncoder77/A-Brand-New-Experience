from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import reviewerRegisterForm, reviewerLoginForm, bloggerRegisterForm, bloggerLoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'index.html')


def creatorPortal(request):
    context = {}
    bloggerSignup = bloggerRegisterForm()
    bloggerLogin = bloggerLoginForm()

    if (request.method == "POST"):
        if ('login' in request.POST):
            bloggerLogin = bloggerLoginForm(request.POST)
            if (bloggerLogin.is_valid()):
                blogger = authenticate(request, username=bloggerLoginForm)



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

def reviewerLogin(request):
    form = reviewerLoginForm()
    if (request.method == 'POST'):
        form = reviewerLoginForm(request.POST)
        if (form.is_valid()):
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if (user is not None):
                login(request, user)

                return redirect('reviewerHome')
            else:
                print("Authentication failed")
                return render(request, 'reviewerLogin.html', context={'form':form})

    return render(request, 'reviewerLogin.html', {'form': form})


'''def bloggerSignUp(request):
    pass'''

@login_required
def reviewerHome(request):
    context = {
        'user' : request.user
    }
    return render(request, 'reviewerHome.html', context)



def logoutUser(request):
    logout(request)
    return redirect('home')