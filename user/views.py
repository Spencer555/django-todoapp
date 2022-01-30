from django.shortcuts import render, redirect
from django.contrib import messages 
from user.forms import UserCreationForm, UserRegisterForm
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username} your account has been created successfully! You can now login to create your todo's all the best.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})