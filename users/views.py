from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Profile
from resume.models import Resume
from .utils import search_profile

from .forms import ProfileForm, CustomUserCreationForm


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ValueError:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password incorrect')

    return render(request, 'users/login-register.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account has been created')

            login(request, user)
            return redirect('edit-account')  # TODO- create url
    else:
        messages.error(request, 'An error has occurred during registration')

    context = {'form': form, 'page': page}
    return render(request, 'users/login-register.html', context)


@login_required(login_url='login')
def profiles(request):
    all_profiles,search_query = search_profile(request)
    contex = {'profiles': all_profiles,'search_query':search_query}
    return render(request, 'users/profiles.html', contex)


@login_required(login_url='login')
def profile(request, pk):
    single_profile = get_object_or_404(Profile, id=pk)
    resumes = Resume.objects.filter(owner=single_profile)
    context = {'profile': single_profile, 'resumes': resumes}
    return render(request, 'users/single-profile.html', context)


@login_required(login_url='login')
def edit_account(request):
    user_account_profile = request.user.profile
    form = ProfileForm(instance=user_account_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES, instance=user_account_profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form, 'profile':user_account_profile}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def user_account(request):
    user_acc = request.user.profile
    resumes = user_acc.resume_set.all()
    context = {'profile': user_acc, 'resumes': resumes}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def user_profile(request, pk):
    single_profile = get_object_or_404(Profile, id=pk)
    resumes = Resume.objects.filter(owner=single_profile)
    context = {'profile': single_profile, 'resumes': resumes}
    return render(request, 'users/single-profile.html', context)
