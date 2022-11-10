from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from Lite.models import register

# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def food(request):
    return render(request,'food.html')
def bmi_calculator(request):
    return render(request,'bmi_calculator.html')

def register(request):
        username=request.POST.get('username')
        height=request.POST.get('height')
        weight=request.POST.get('weight')
        gender=request.POST.get('gender')
        email=request.POST.get('email')
        password=request.POST.get('password')
        r=register(username=username,height=height,weight=weight,gender=gender,email=email,password=password)
        r.save()
        return render(request,"home.html")
'''
        form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"home.html")
'''
def login(request):
    return render(request,"food.html")
    if request.method=="POST":
        count=register.objects.all().count()
        x=0
        for i in range(count):
            username=register.objects.all()[i].username
            height=register.objects.all()[i].height
            weight=register.objects.all()[i].weight
            gender=register.objects.all()[i].gender
            email=register.objects.all()[i].email
            password=register.objects.all()[i].password
            if (username==Username and  password==Password ):
                x=0
                break
            else:
                x+=1
        if (x==0):
            print("login successfully")
        else:
            print("login unsuccessful")

    
