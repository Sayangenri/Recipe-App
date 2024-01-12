from django.shortcuts import render, redirect,HttpResponse
from .models import Logindb
def login(request):
    if request.method == 'POST':
        lemail = request.POST.get("email")
        lpassword = request.POST.get("password")
        try:
            user = Logindb.objects.get(email=lemail)
            if user.password == lpassword:
              return redirect('/recipe')
            else:
                error_message = 'Invalid password'
                return render(request, 'login.html', {'error_message': error_message})
        except Logindb.DoesNotExist:
            error_message = 'Email not found'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
      lname=request.POST.get("name")
      lemail=request.POST.get("email")
      lpassword=request.POST.get("password")
      Logindb.objects.create(name=lname,email=lemail,password=lpassword)
      return redirect('/')
    return render(request,'register.html')
