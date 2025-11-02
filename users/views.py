from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST': #اذا المستخدم ادخل المعلومات وضغط  موافق
        form = RegisterForm(request.POST)#request.POST contains the submitted data from the form.
        #You dont pass the entire request object to the form—just the POST data.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')#يجيب اليوزرنيم الي المستخدم ادخله
            messages.success(request,f'Welcome {username} your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
  
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    return render(request,'users/profile.html')