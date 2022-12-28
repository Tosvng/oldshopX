import json
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import MemberForm

# Create your views here.


def landing_page(request):
    context = {}
    if request.method == "GET":
        return render(request, "server/landingPage.html", {})

    elif request.method == "POST":
        # get the email from the form
        email = request.POST['email']
        # use the automated emailer API to send the user an email
        url = f"https://automated-reply.herokuapp.com/email/{email}/Welcome!"
        response = requests.get(url)

        # convert the response to a dictionary
        response_dict = response.json()

        # redirect the user based on the API response
        if (response_dict['success']):
            # send_email("Thank you for your purchase", email)
            return redirect('server:confirmation_page')
        else:
            return 'You have already claimed your trail!'


def confirmation_page(request):
    if request.method == "GET":
        return render(request, "server/confirmationPage.html", {})


def create(request):
    if (request.method == "GET"):
        return render(request, "server/createAccountPage.html", {})
    elif (request.method == "POST"):
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        # DONT FORGET TO CHANGE THIS
        return render(request, "server/confirmationPage.html", {})
