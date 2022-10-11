from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

from .models import Profile
from main.models import Select, Option

# Create your views here.
def voting(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        gender = request.POST['gender'] # check html page for gender if radio button wrks correct
        department = request.POST['department']
        person = request.POST['person'] # check this too for select menu

        if (person and firstname) and lastname != None:
            if User.objects.filter(first_name=firstname).exists() and User.objects.filter(last_name=lastname).exists():
                messages.info(request, "Sorry it seems you have already voted") #it is temporary this must be done for facial image
                return redirect("voting")
            else:
                user = User.objects.create_user(username = firstname + lastname)
                user.save()

                #log user in and redirect to settings page

                #create a profile object for the new user
                user_model = User.objects.get(username = firstname + lastname)
                new_profile = Profile.objects.create(
                    user=user_model, 
                    id_user=user_model.id,
                    
                    )
                new_profile.save()
                return redirect("addface")
        else:
            messages.info(request, 'Invalide Credentials')
            return redirect("voting")

    else:
        options = Select.objects.all()
        # choices = []
        # for i in range(Option.request.no_of_choices):
        #     choice = Select.objects.get(request.opt, pk=i+1)
        #     choices.append(choice)
        return render(request, "basiclayer/form.html", {
            'options': options
        }) # here choices are the same list used for signup

# def getoptions(request):
#     choices
#     options = CreateVote.objects.get(user=request.user)
#     return HttpResponse("choice")

def addface(request):
    return render(request, 'basiclayer/face.html')