"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from firstApp.views import employeeView
from rest_framework.routers import DefaultRouter
from mixinApp import views

router = DefaultRouter()
router.register('course',views.CourseViewSet) 


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('emp/',employeeView),
    #path('firstApp/',include('firstApp.urls')),
    #path('fbvSerializers/',include('fbvSerializers.urls')),
    #path('cbvSerializers/',include('cbvSerializers.urls')),
    #path('mixinApp/',include('mixinApp.urls')),
    path('courses/',include(router.urls)),

]
