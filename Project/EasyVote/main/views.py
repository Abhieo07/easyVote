from random import randint
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

from .models import CreateVote, Option, Select
from basiclayer.urls import *
       
# Create your views here.
#function to be imported for option menu

code = str(randint(100000, 1000000))

def index(request):
    return render(request, 'main/index.html')


@login_required(login_url='index') # this is for login
def home(request):
    # x = User.objects.get('generated-code')
    # return render(request, "main/status.html", {
    #     'x': x
    # })
    return render(request, 'main/index.html')

def section(request, part):
    if part == "create":

        if request.method == 'POST':
            username = request.POST['projectname']
           # password = request.POST['password']
            discription = request.POST['discription']
            no_of_choice = request.POST['no_of_choices']
            
            option = Option.objects.create(no_of_choices=no_of_choice, discription=discription)
            option.save()

            for i in range(int(no_of_choice)):
                choice = request.POST[f'option{i+1}']
                select = Select.objects.create(opt=choice)
                select.save()
            
            if no_of_choice is not None:
                if username is None:
                    messages.info(request, "Invalid project name")
                    return HttpResponseRedirect('index')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, "Project name is taken taken")
                    return HttpResponseRedirect('index')
                else:
                    user = User.objects.create_user(
                        username=username,
                         
                        password=code,
                         #here i got doubt this might work
                        )
                    user.save()
                    

                    #log user in and redirect to status page where the creator can see the status of vote
                    user_login = auth.authenticate(username=username, password=code)
                    auth.login(request, user_login)

                    #create a profile object for the new user
                    user_model = User.objects.get(username = username)
                    new_profile = CreateVote.objects.create(user=user_model, id_user=user_model.id)
                    new_profile.save()
                    return HttpResponseRedirect('status')
            else:
                messages.info(request, 'Invalid code')
                return HttpResponseRedirect('index')

        else:
            return render(request, 'main/index.html')
    
    elif part == "vote":
        if request.method == 'POST':
            username = request.POST['projectname']
            password = request.POST['generated_code']

            user = auth.authenticate(username=username, password=password) #there might be username = projectname

            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('voting')
            else:
                messages.info(request, 'Credentials Invalid')
                return HttpResponseRedirect('index')
        else:
            return render(request, 'main/index.html')

    else:
        raise Http404("Invalid Selection")

@login_required(login_url='index')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('main/index')

def status(request):
    return render(request, 'main/status.html', {
        'projectname': request.user.username,
        'code': code
    })