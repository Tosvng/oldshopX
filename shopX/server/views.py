import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# for automated email
# from dotenv import load_dotenv
import os
import ssl
import smtplib
import requests
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

# Create your views here.


def landing_page(request):
    context = {}
    if request.method == "GET":
        return render(request, "server/landingPage.html", {})

    elif request.method == "POST":
        # get the email from the form
        email = request.POST['email']
        # use the automated emailer API to send the user an email
        url = f"https://automated-reply.herokuapp.com/email/{email}"
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
