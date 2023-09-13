from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password!=get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,'Email already used')
            return redirect('/auth/signup/')
          
        except:
            pass

        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()

        user = authenticate(request, username=get_email, password=get_password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User created Login success')
            return redirect('/')

        messages.success(request,'User is created please Login')
        return render(request,'login.html')

    return render(request,'signup.html')


def handleLogin(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')

        user = authenticate(request, username=get_email, password=get_password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login success')
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')




def handleLogout(request):
    logout(request)
    messages.success(request,'Logout Success')
    return render(request,'login.html')
