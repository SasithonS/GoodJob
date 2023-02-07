from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateEmpUserForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

@register.filter(name='show_error')
def show_error(dictionary):
    try:
        return list(dictionary.values())[0][0]
    except (TypeError,IndexError,AttributeError):
        return 'try again'

# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        if EmployerUser.objects.filter(user=request.user.id).exists():
                    return redirect('home_emp')
        elif JobberUser.objects.filter(user=request.user.id).exists():
            return redirect('home_jobber')
        elif AdminUser.objects.filter(user=request.user.id).exists():
            return redirect('admin_jobber')
        else:
            if request.user.last_name :
                return redirect('home_emp')
            else:
                return redirect('home_jobber')
    else:
        if request.method == 'POST':

            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if EmployerUser.objects.filter(user=user).exists():
                    return redirect('home_emp')
                elif JobberUser.objects.filter(user=user).exists():
                    return redirect('home_jobber')
                elif AdminUser.objects.filter(user=user).exists():
                    return redirect('admin_jobber')
                else: 
                    if user.last_name :
                        return redirect('home_emp')
                    else:
                        return redirect('home_jobber')
            else:
                error = 'Invalid username or password'
                return render(request, 'users/login.html',{'error':error})

        context = {}
        return render(request, 'users/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.user.is_authenticated:
        return redirect('home_admin')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'users/signup.html', context)

def reset_password(request):
    return render(request, 'users/password_reset_email.html')


def signup_emp(request):
    if request.user.is_authenticated:
        return redirect('home_emp')
    else:
        form = CreateEmpUserForm()
        if request.method == 'POST':
            form = CreateEmpUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'users/signup_emp.html', context)


# def signup_emp(request):
#     users = User.objects.filter(id=id)
#     province = Province.objects.all()

#     if request.method == 'POST':
#         emp = EmployerUser()
#         emp.user = User.objects.get(id=id)
#         emp.emp_name = request.POST.get('name')
#         emp.email = request.POST.get('email')
#         if request.POST.get('emp_name'):
#             emp.name = request.POST.get('emp_name')
#         if request.POST.get('phone'):
#             emp.phone = request.POST.get('phone')
#         if request.POST.get('province'):
#             emp.province = Province.objects.get(province=request.POST.get('province'))
#         emp.address = request.POST.get('address')
#         emp.location = request.POST.get('location')
#         emp.picture = request.FILES['picture']
#         emp.save()
#         return redirect('login')

    # context = {'users': users,'province':province}
    # return render(request, 'users/signup_emp.html', context)


@login_required(login_url='login')
def jobber_profile(request,id):
    users = User.objects.filter(id=id)
    return render(request, 'users/jobber_profile.html', {'users': users})

@login_required(login_url='login')
def jobber_update(request,id):
    users = User.objects.filter(id=id)
    gender = Gender.objects.all()
    education = Education.objects.all()
    province = Province.objects.all()

    if request.method == 'POST':
        user = User.objects.get(id=id)
        jobber = JobberUser()
        jobber.user = user
        jobber.name = user.first_name
        jobber.email = request.POST.get('email')
        if request.POST.get('phone'):
            jobber.phone = request.POST.get('phone')
        if request.POST.get('age'):
            jobber.age = request.POST.get('age')
        if request.POST.get('gender'):
            jobber.gender =  Gender.objects.get(gender=request.POST.get('gender'))
        if request.POST.get('education'):
            jobber.education = Education.objects.get(education=request.POST.get('education'))
        if request.POST.get('province'):
            jobber.province = Province.objects.get(province=request.POST.get('province'))
        jobber.address = request.POST.get('address')
        jobber.location = request.POST.get('location')
        jobber.picture = request.FILES['picture']
        jobber.save()
        return redirect('jobber_profile',id=id)

    context = {'users': users,'gender':gender,'education':education,'province':province}
    return render(request, 'users/jobber_update.html', context)

@login_required(login_url='login')
def jobber_check(request,id):
    users = User.objects.filter(id=id)
    if request.method == 'POST':
        user = User.objects.get(id=id)
        jobber_check = JobberCheck()
        jobber_check.jobber = JobberUser.objects.get(name=user.first_name)
        jobber_check.identity_pic = request.FILES['picture']
        jobber_check.save()
        return redirect('jobber_profile',id=id)

    context = {'users': users}
    return render(request, 'users/jobber_check.html', context)


@login_required(login_url='login')
def emp_check(request,id):
    users = User.objects.filter(id=id)
    gender = Gender.objects.all()
    if request.method == 'POST':
        user = User.objects.get(id=id)
        employer_check = EmployerCheck()
        employer_check.employer = EmployerUser.objects.get(user=user)
        employer_check.identity_pic = request.FILES['picture']
        employer_check.save()
        return redirect('emp_profile',id=id)

    context = {'users': users,'gender':gender}
    return render(request, 'users/emp_check.html', context)

@login_required(login_url='login')
def emp_profile(request,id):
    users = User.objects.filter(id=id)
    return render(request, 'users/emp_profile.html', {'users': users})

@login_required(login_url='login')
def emp_update(request,id):
    users = User.objects.filter(id=id)
    province = Province.objects.all()

    if request.method == 'POST':
        emp = EmployerUser()
        emp.user = User.objects.get(id=id)
        emp.emp_name = request.POST.get('name')
        emp.email = request.POST.get('email')
        if request.POST.get('emp_name'):
            emp.name = request.POST.get('emp_name')
        if request.POST.get('phone'):
            emp.phone = request.POST.get('phone')
        if request.POST.get('province'):
            emp.province = Province.objects.get(province=request.POST.get('province'))
        emp.address = request.POST.get('address')
        emp.location = request.POST.get('location')
        emp.picture = request.FILES['picture']
        emp.save()
        return redirect('emp_profile',id=id)

    context = {'users': users,'province':province}
    return render(request, 'users/emp_update.html', context)

@login_required(login_url='login')
def admin_profile(request,id):
    users = User.objects.filter(id=id)
    return render(request, 'users/admin_profile.html', {'users': users})

@login_required(login_url='login')
def admin_update(request,id):
    users = User.objects.filter(id=id)
    if request.method == 'POST':
        admin = AdminUser()
        admin.user = User.objects.get(id=id)
        admin.name = request.POST.get('name')
        admin.email = request.POST.get('email')
        admin.picture = request.FILES['picture']
        admin.save()
        return redirect('admin_profile',id=id)

    context = {'users': users}
    return render(request, 'users/admin_update.html', context)
