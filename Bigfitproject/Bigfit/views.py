
from django.shortcuts import render,redirect,HttpResponse
from . import models
from .forms import UserForm,RegisterForm,WeightinputForm
from django.contrib.auth import login as guest_login,authenticate
import datetime

def index(request):
    pass
    return render(request, 'index.html')


def login(request):

    if request.session.get('is_login',None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check your input"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(username=username)
                if user is not None:
                    guest_login(request, user)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "Password is not correct.！"
            except:
                message = "User does not exist."
        return render(request, 'login.html', locals())
    login_form = UserForm()
    return render(request, 'login.html', locals())

def register(request):

    if request.session.get('is_login',None):
        return redirect('/index')

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Please check your input！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            target_weight = register_form.cleaned_data['target_weight']
            feet = register_form.cleaned_data['feet']
            inches = register_form.cleaned_data['inches']
            date_of_birth = register_form.cleaned_data['date_of_birth']
            zip_code = register_form.cleaned_data['zip_code']
            gender = register_form.cleaned_data['gender']

            if password1 != password2:
                message = "The password entered twice is different！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message = 'The user already exists, please re-select the username!'
                    return render(request, 'register.html', locals())

                new_user = models.User.objects.create()
                new_user.username = username
                new_user.password = password1
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.target_weight = target_weight
                new_user.feet = feet
                new_user.inches = inches
                new_user.date_of_birth = date_of_birth
                new_user.zip_code = zip_code
                new_user.gender = gender
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def weightinput(request):
    if request.method == "POST":
        weightinput_form = WeightinputForm(request.POST)
        if weightinput_form.is_valid():
            cweight = weightinput_form.cleaned_data['current_weight']

            new_weight = models.WeightTracker.objects.create()
            new_weight.user_id = request.user.id
            new_weight.weight = cweight
            new_weight.save()

            return redirect('/index/')
    weightinput_form = WeightinputForm
    return render(request, 'weightinput.html',locals())

def weighthistory(request):
    current_id = request.user.id
    weight_tracker_list_obj = models.WeightTracker.objects.filter(user_id=current_id)
    return render(request, 'weighthistory.html',{'li':weight_tracker_list_obj})