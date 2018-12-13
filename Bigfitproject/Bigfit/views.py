from django.shortcuts import render, redirect, HttpResponse
from . import models
from .forms import UserForm,RegisterForm, WeightinputForm
from django.contrib.auth import login as guest_login, authenticate
import datetime


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def viewprofile(request):
    current_id = request.user.id
    profile_list = models.User.objects.filter(id=current_id)
    return render(request,'profile.html',{'uli':profile_list})

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
                    message = "Password is not correct！"
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
                message = "Passwords do not match！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(username=username)
                if same_name_user:
                    message = 'The user already exists, please enter another username!'
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
            new_weight = models.WeightTracker.objects.create(weight=cweight, user=request.user)
            return redirect('/index/')
    weightinput_form = WeightinputForm
    return render(request, 'weightinput.html', locals())

def weighthistory(request):
    current_id = request.user.id
    weight_tracker_list_obj = models.WeightTracker.objects.filter(user_id=current_id)
    return render(request, 'weighthistory.html', {'li': weight_tracker_list_obj})

def deleteweighthistory(request):
    cid = request.user.id
    nid = request.GET.get('nid')
    models.WeightTracker.objects.filter(user_id=cid, id=nid).delete()
    return redirect('/index/')

def editweighthistory(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj = models.WeightTracker.objects.filter(id=nid).first()
        return render(request, 'editweight.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        nid = request.GET.get('nid')
        uweight = request.POST.get('title')
        models.WeightTracker.objects.filter(user_id=cid, id=nid).update(weight=uweight)
        return redirect('/index/')

def editusername(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editusername.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        username = request.POST.get('username')
        models.User.objects.filter(id=cid).update(username=username)
        return redirect('/index/')

def edittargetweight(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'edittargetweight.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        targetweight = request.POST.get('targetweight')
        models.User.objects.filter(id=cid).update(target_weight=targetweight)
        return redirect('/index/')

def editgender(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editgender.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        gender = request.POST.get('gender')
        models.User.objects.filter(id=cid).update(gender=gender)
        return redirect('/index/')

def editfeet(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editfeet.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        feet = request.POST.get('feet')
        models.User.objects.filter(id=cid).update(feet=feet)
        return redirect('/index/')

def editinches(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editinches.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        inches = request.POST.get('inches')
        models.User.objects.filter(id=cid).update(inches=inches)
        return redirect('/index/')

def editzipcode(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editzipcode.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        zipcode = request.POST.get('zipcode')
        models.User.objects.filter(id=cid).update(zip_code=zipcode)
        return redirect('/index/')

def editdob(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editdob.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        dob = request.POST.get('dob')
        models.User.objects.filter(id=cid).update(date_of_birth=dob)
        return redirect('/index/')

def editpassword(request):
    if request.method == 'GET':
        cid = request.user.id
        obj = models.User.objects.filter(id=cid).first()
        return render(request, 'editpassword.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.user.id
        pw1 = request.POST.get('password1')
        pw2 = request.POST.get('password2')
        if pw1 == pw2:
            models.User.objects.filter(id=cid).update(password=pw1)
            return redirect('/index/')
        else:
            message = "Passwords do not match！"
            return render(request,'editpassword.html',locals())