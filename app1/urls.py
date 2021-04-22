""" newprjct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views


# for api view as class based
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('',views.view_api)





urlpatterns = [

    path('index/', views.index, name= 'index page'),
    path('profile/', views.profile, name='Profile Page'),
    path('crud_page/', views.person.as_view()),
    path('', views.person.as_view()),
    path('create/',views.create, name="create page"),
    path('update/<str:id>',views.update, name = 'Update Page'),
    path('delete/<str:id>',views.delete, name = 'Delete Page'),
    path('<int:pk>', views.LeadDetailView.as_view()),
    path('api_view/',views.asad, name= 'API View'),
    path('put_data/',views.put_data, name= 'put data'),
    path('view_api/', include(router.urls)),
    path('registration/',views.loginprps, name='Registration Page'),
    path('signup/',views.signupview.as_view(), name = 'signup page'),
    path('login/',views.userlogin)

]
