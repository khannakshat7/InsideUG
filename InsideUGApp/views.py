from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from InsideUGApp.forms import UserForm
from InsideUGApp.models import Course,Books
# Create your views here.

def index(request):
    course = Course.objects.all()[:8]
    books = Books.objects.all()[:8]
    return render(request,'index.html',{"courses":course,"books":books})

def books(request):
    all_books = Books.objects.all()
    return render(request,'books.html',{"books":all_books})

def courses(request):
    all_course = Course.objects.all()
    return render(request,'courses.html',{"courses":all_course})

def category(request,cat):
    if(cat=='Engineering'):
        cat_course = Course.objects.filter(stream='btech')
    return render(request,'catagories.html',{"category":cat,"courses":cat_course})

@csrf_exempt
def addcourse(request):
    if(request.method == 'POST'):
        try:
            stream = request.POST.get('course')
            branch = request.POST.get('branch')
            title = request.POST.get('title')
            disc = request.POST.get('disc')
            link = request.POST.get('link')
            imageSmall = request.FILES['imgsmall']
            imageBig = request.FILES['imgbig']
            
            course = Course()
            course.stream = stream
            course.branch = branch
            course.title = title
            course.link = link
            course.discription = disc
            course.smallImage = imageSmall
            course.BigImage = imageBig
            course.save() 
            data = {
                "msg": "The course added successfully!!"
            }
        except:
            data = {
                "err": "An error occured in adding the course"
            }
        return render(request,'addcourse.html',data)
    else:
        return render(request,'addcourse.html')

@csrf_exempt
def addbook(request):
    if(request.method == 'POST'):
        try:
            stream = request.POST.get('course')
            branch = request.POST.get('branch')
            title = request.POST.get('title')
            disc = request.POST.get('disc')
            link = request.POST.get('link')
            imageSmall = request.FILES['imgsmall']
            imageBig = request.FILES['imgbig']
            
            book = Books()
            book.stream = stream
            book.branch = branch
            book.title = title
            book.link = link
            book.discription = disc
            book.smallImage = imageSmall
            book.BigImage = imageBig
            book.save() 
            data = {
                "msg": "The Book added successfully!!"
            }
        except:
            data = {
                "err": "An error occured in adding the Book!!"
            }
        return render(request,'addbook.html',data)
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
            login(request,user)
            msg={"message":True}
            return redirect('/')
        else:
            error={"error":True}
            return render(request,"login.html",error)
    else:
        return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect('/')

@login_required
def MBAFile(request):
    if (request.user.is_authenticated):
        return redirect("../media/Marketing_Dossier.pdf")
    else:
        return redirect("login")