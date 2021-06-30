from django.shortcuts import render, redirect, HttpResponse
import bcrypt
from django.contrib import messages
from .models import User


def index(request):
    return render(request, 'login_reg.html')

def register(request):
        if request.method == 'POST':
            errors = User.objects.reg_validator(request.POST)
            if len(errors) > 0:
                for key,value in errors.items():
                    messages.error(request, value)
                return redirect('/')

        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        user = User.objects.create(
                name = request.POST['name'],
                alias = request.POST['alias'],
                email = request.POST['email'],
                password = hash_pw
            )
        request.session['logged_user'] = user.id
        return redirect('/profile')


def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect('/profile')
        messages.error(request, "username or password are incorrect.")
    return redirect('/') 

def profile(request):
    if 'logged_user' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['logged_user'])
    context = {
        'curr_user': user
    }
    return render(request, 'profile.html', context)

def add_book(request):
    return render(request, 'addbook.html')

def logout(request):
    request.session.flush()
    return redirect('/')





