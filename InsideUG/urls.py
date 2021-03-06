"""InsideUG URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from InsideUGApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('books/', views.books, name='books'),
    path('courses/', views.courses, name='courses'),
    path('category/<path:cat>/', views.category, name='category'),
    path('news/', views.category, name='news'),
    path('login/', views.loginuser, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutuser, name='logout'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('addbook/', views.addbook, name='addbook'),
    path('addnews/', views.addnews, name='addnews'),
    path('mba/', views.MBAFile, name='MBAFile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
