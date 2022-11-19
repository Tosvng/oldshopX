from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# for automated email
# from dotenv import load_dotenv
import os
import ssl
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path


# load_dotenv()  # take environment variables from .env.
# sender_email = os.environ.get("SENDER_EMAIL")
# password = os.environ.get("PASSWORD")

sender_email = "altosintiams@gmail.com"
password = "nuydxwnxmqzapsjk"

PORT = 465
EMAIL_SERVER = "smtp.gmail.com"


def send_email(subject, receiver_email):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("ShopX", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    body = '''Hi,
    I hope you are well.
    '''

    msg.set_content(body)

    context = ssl.create_default_context()
    # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    # msg.add_alternative(
    #     f"""\
    # <html>
    #   <body>
    #     <p>Hi ,</p>
    #     <p>I hope you are well.</p>
    #     <p>I just wanted to drop you a quick note to remind you that <strong> USD</strong> in respect of our invoice is due for payment on <strong></strong>.</p>
    #     <p>I would be really grateful if you could confirm that everything is on track for payment.</p>
    #     <p>Best regards</p>
    #     <p>YOUR NAME</p>
    #   </body>
    # </html>
    # """,
    #     subtype="html",
    # )

    with smtplib.SMTP_SSL(EMAIL_SERVER, PORT, context=context) as server:
        # server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
# Create your views here.


def landing_page(request):
    context = {}
    if request.method == "GET":
        return render(request, "server/landingPage.html", {})

    elif request.method == "POST":
        email = request.POST['email']
        user_exist = False
        # check if this email has already been used
        # try:
        #     User.objects.get(email=email)
        #     user_exist = True
        # except:
        #     pass
        # if not user_exist:
        #     user = User.objects.create_user(email=email)
        #     return redirect('server:confirmation_page')
        # else:
        #     context['message'] = "User already exists."
        #     return render(request, 'server/landingPage.html', context)

        # for testing
        print(email)
        send_email("Thank you for your purchase", email)
        return redirect('server:confirmation_page')


def confirmation_page(request):
    if request.method == "GET":
        return render(request, "server/confirmationPage.html", {})
