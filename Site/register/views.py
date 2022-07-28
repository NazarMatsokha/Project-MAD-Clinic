from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST': #якшо передали якийсь пост то:
        form = UserRegisterForm(request.POST) #створю об'єкт форми і заповню її данними із поста
        if form.is_valid(): # проводжу валідацію
            form.save()#якшо все ок зберігаю форму
            messages.success(request, 'Ви успішно зареєструвались')#імпортував повідомлення для того шобпрт успішному збереженні вибити повідомлення
            return redirect('login')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()#в іншому випадку це буде несвязана форма
    return render(request, 'register/register.html', {"form": form})

def login_user(request):
    form_class = UserLoginForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
        else:
            form = UserLoginForm()
    return render(request, 'register/login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('main_page')
