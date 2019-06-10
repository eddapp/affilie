from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import pyrebase
from django.contrib import auth

config = {

    'apiKey': "AIzaSyBzS6cYXT6bW3rsX59PCOE104U2j92iG8s",
    'authDomain': "django-framework-48359.firebaseapp.com",
    'databaseURL': "https://django-framework-48359.firebaseio.com",
    'projectId': "django-framework-48359",
    'storageBucket': "django-framework-48359.appspot.com",
    'messagingSenderId': "1035375680898"
}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database = firebase.database()

def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"
        return render(request, "signIn.html", {"messg": message})
    print(user['idToken'])
    session_id = user['idToken']
    request.session['uid'] = str(session_id)
    return render(request, "welcome.html", {"e": email})


def logout(request):
    auth.logout(request)
    return render(request, 'signIn.html')


def signup(request):
    return render(request, "signUp.html")


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.p.get('pass')

    user = authe.create_user_with_email_and_password(email, passw)
