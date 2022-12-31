from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
import string
import random
from .forms import *
from .models import *
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import uuid
from presence_app.settings import EMAIL_HOST_USER, APP_HOST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def generate_password():
    characters = list(string.ascii_letters + string.digits + "@#$%&")
    random.shuffle(characters)
    password = []
    for i in range(8):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    password = "".join(password)
    return password

def generate_username():
    characters = list(string.ascii_uppercase + string.digits)
    random.shuffle(characters)
    username = []
    for i in range(8):
        username.append(random.choice(characters))
        
    random.shuffle(username)
    username = "".join(username)
    return username
        
def send_mail_function(subject, message, email):
    try:
        subject = f"SGP: {subject}"
        from_email = EMAIL_HOST_USER
        content_html = 'vues/send_mail_function.html'
        app_host = APP_HOST
        context = {
            'message': message,
            'app_host': app_host,
        }
        html_render = render_to_string(content_html, context)
        message_send = EmailMultiAlternatives(subject, "", from_email, [email])
        message_send.attach_alternative(html_render, "text/html")
        message_send.send()
    except Exception as e:
        error_html = f"<html><body><h2>Error system: {e}</h2></body></html>"
        return HttpResponse(error_html)
