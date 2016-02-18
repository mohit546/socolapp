from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import admin
from django.db import IntegrityError

def loginMaster(request):
    return render_to_response('html_template/login/loginIndex.html')

def user_login(request):
    print request.body
    data_dict = json.loads(request.body)
    print request.COOKIES

    username = data_dict['username']
    password = data_dict['password']

    user = auth.authenticate(username=username,password=password)
    print user
    print username, password
    if user is not None:
        if user.is_active:
            auth.login(request,user)
            print "Login Successful"
            return HttpResponse(json.dumps({"validation":"Login Successful","status":True,'redirecturl':"/userHome"}), content_type="application/json")
        else:
            print "Login Failed"
            return HttpResponse(json.dumps({"validation":"Invalid Login","status":False}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({"validation":"Invalid Login Credentials","status":False}), content_type="application/json")


def signIn(request):
    return render_to_response('html_template/login/signIn.html')

def signUp(request):
    return render_to_response('html_template/login/signUp.html')
