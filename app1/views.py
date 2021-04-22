from django.shortcuts import render

# Create your views here.
from .models import mymodel

from .forms import web,user_login_form

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView

from rest_framework.views import APIView
from .serializer import frnd
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import viewsets

# for login
from .forms import logon
from django.views.generic import CreateView

from django.contrib.auth import views,login,authenticate



def index(request):
     context={
         'name':"Ashwin", 'name1':'Somy','name2':'sunil'
     }
     return render(request, 'index.html',context=context)

def profile(request):

    return render(request, 'profile.html',{'title':'Django Page','link':'http://google.com'})



def fc1(request):
    s = mymodel.objects.all()
    context = {'s':s }
    return  render(request,'crud temp.html',context=context)




# CRUDE Operations
# Create Operations
def create(request):
    form = web()
    context = {'form':form}
    if request.method == 'POST':
        form = web(request.POST)
        form.save()

    return render(request,'forms.html',context=context)


# Update Operation
def update(request,id):
    ud = mymodel.objects.get(pk= id)
    form = web(instance=ud)

    if request.method == 'POST':
        form = web(request.POST)
        if form.is_valid():
            form.save()


    return render(request,'forms.html',{'form':form })




# Delete Operation

def delete(request,id):
    dt = mymodel.objects.get(pk = id)
    dt.delete()
    return  HttpResponse('Data deleted successfully')




# Class Based Views


class person(ListView):
    template_name = 'crud temp.html'
    queryset  = mymodel.objects.all()
    context_object_name = 's'


#detailview

class LeadDetailView(DetailView):
      template_name = 'detailview.html'
      queryset = mymodel.objects.all()
      context_object_name = "s"



#API View

@api_view(['GET'])
def asad(request):
    all_data = mymodel.objects.all()
    serial_data = frnd(all_data,many=True)
    return Response(serial_data.data)


@api_view(['POST'])
def put_data(request):
    serial_data = frnd(data = request.data)
    if serial_data.is_valid():
        serial_data.save()

    return Response(serial_data.data)


class view_api(viewsets.ModelViewSet):
    serializer_class = frnd
    queryset = mymodel.objects.all()



#user login

def loginprps(request):
    form = logon()
    if request.method=='POST':
        form = logon(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'forms.html',{'form':form})


class signupview(CreateView):
    form_class = logon
    template_name = 'forms.html'


def userlogin(request):
    form = user_login_form()
    context = {'form':form, 'name':'login'}
    if request.method == 'POST':
        user_name = request.POST['user_name']
        psswd = request.POST['psswd']
        user = authenticate(user_name=user_name,psswd=psswd)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse('<h2> Invalid User </h2>')
    return render(request,'forms.html',context=context)