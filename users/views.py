from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User, Group


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            account_type = form.cleaned_data.get('account_type')
            if account_type == "1":
                new_user = User.objects.create_user(username, email, password1)
                new_user.is_staff = True
                new_user.save()
                group = Group.objects.get(name='Authors')
                new_user.groups.add(group)
                messages.success(request, f'Your "Author" account has been created! Now you may Log In!')
            else:
                form.save()
                messages.success(request, f'Your account has been created! Now you may Log In!')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

