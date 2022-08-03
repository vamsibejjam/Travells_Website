from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User


# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['First']
        last_name=request.POST['Last']
        user_name=request.POST['user']
        password_1=request.POST['pwd1']
        password_2=request.POST['pwd2']
        email=request.POST['mail']
        

        if password_1==password_2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,password=password_1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect('login')

        else:
            messages.info(request,'passwords not matching')
            return redirect('register')
        
        
    else:
        return render(request,'Register.html')


def login(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pwd=request.POST['pwd']
        
        user=auth.authenticate(username=user_name,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'Invalid Users')
            return redirect('login')

    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def book(request):
    if request.method=='POST':
        dest=request.POST['inputcity']
        car=request.POST['car']
        passengers=request.POST['persons']
        home=request.POST['inputCity']
        mobile=request.POST['phone']
        address=request.POST['address2']
        Travel_date=request.POST['travel_date']
        form={'city':home,'address':address,'vehicle':car,'date':Travel_date,'phone':mobile,'passengers':passengers
        ,'spot':dest}
        messages.info(request,'Congrats!.. your booking is done.')
        
        return render(request,'Booked_form.html',form)

    else:
        return render(request,'Tour_register.html')

