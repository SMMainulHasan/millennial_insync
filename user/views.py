from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from user.forms import UserRegistrationForm


#USER REGISTRATION
def user_registration(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            login(request, user)
            return redirect("profile")
    
    return render(request, 'user/registration.html', {'form': form})


#USER LOG_IN
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is True:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("login")
    
    return render(request, 'user/login.html')


#USER LOG_OUT
def user_logout(request):
    logout(request)
    return redirect("home")