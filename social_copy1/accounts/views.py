from django.shortcuts import render
from . models import UserProfileInfo
from .forms import UserProfileInfoForm, UserInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
# Create your views here.


def sign_up(request):
    registered = False
    if request.method == 'POST':
        user_form = UserInfoForm(request.POST)
        profile_form = UserProfileInfoForm(request.FILES, request.POST)

        if user_form.is_valid() and profile_form.is_valid() and user_form.cleaned_data['password'] == user_form.cleaned_data['confirm_password']:
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            raise ValueError(user_form)
    else:
        user_form = UserInfoForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'accounts/sign_up.html', {'user_form': user_form, 'profile_form': profile_form,
                                                     'registered': registered})


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('test'))
            else:
                return HttpResponse('You are not active Try contacting Admin :(')
        else:
            return render(request, 'index.html')

    else:
        return render(request, 'Login.html', {})