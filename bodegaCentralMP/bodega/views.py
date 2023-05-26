#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Credenciales inválidas. Inténtalo nuevamente.'
            return render(request, 'pages/login.html', {'error_message': error_message})
    return render(request, 'pages/login.html')

def index_view(request):
    if request.user.is_authenticated:
        return render(request, 'pages/index.html')
    else:
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')
