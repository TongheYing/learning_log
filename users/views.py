from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def logout_view(request):
    """logout users"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """register new users"""
    if request.method != 'POST':
        # show empty register table
        form = UserCreationForm()
    else:
        # cope with finished table
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # let users log in automately and redirect to main page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)