from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from InsideUGApp.forms import UserForm
from InsideUGApp.models import Course
# Create your views here.

def index(request):
    return render(request,'index.html')

def books(request):
    return render(request,'books.html')

def courses(request):
    return render(request,'courses.html')

def category(request,cat):
    return render(request,'catagories.html',{"category":cat})

@csrf_exempt
def addcourse(request):
    if(request.method == 'POST'):
        stream = request.POST.get('course')
        branch = request.POST.get('branch')
        title = request.POST.get('title')
        disc = request.POST.get('disc')
        imageSmall = request.FILES['imgsmall']
        imageBig = request.FILES['imgbig']
        print(stream,branch,title,disc,imageSmall,imageBig)
        course = Course()
        course.stream = stream
        course.branch = branch
        course.title = title
        course.discription = disc
        course.smallImage = imageSmall
        course.BigImage = imageBig
        course.save() 
        return HttpResponse("Done")
    else:
        return render(request,'addcourse.html')

def addbook(request):
    if(request.method == 'POST'):
        pass
    else:
        return render(request,'addbook.html')

def addnews(request):
    if(request.method == 'POST'):
        pass
    else:
        return render(request,'addnews.html')

def loginuser(request):

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return render(request,"login.html",{"err":True})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return render(request,"login.html",{"invalid":True})
    else:
        return render(request, 'login.html')


def register(request):
    registeredcheck = False
    if(request.method == 'POST'):
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = True
            user.save()
            registeredcheck = True
            msg={"message":True}
            return render(request,'login.html')
        else:
            error={"error":True}
            return render(request,"login.html",error)
    else:
        return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/')