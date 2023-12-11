from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Profile
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
            return redirect('profile')
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
    all_profiles = Profile.objects.all()
    contex = {'profiles': all_profiles}
    return render(request, 'users/profiles.html', contex)


@login_required(login_url='login')
def profile(request, pk):
    single_profile = get_object_or_404(Profile, id=pk)
    context = {'profile': single_profile}
    return render(request, 'users/form-profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    user_profile = request.user.profile
    form = ProfileForm(instance=user_profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/form-profile.html', context)


@login_required(login_url='login')
def user_account(request):
    user_acc = request.user.profile
    context = {'profile': user_acc}
    return render(request, 'users/account.html', context)
