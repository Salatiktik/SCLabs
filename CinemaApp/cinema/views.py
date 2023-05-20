import requests
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import LoginForm, SignUpForm
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.

class HomeView(View):
    def get(self, req, *args, **kwargs):
        return render(req,'cinema/home.html')

class LoginView(View):
    form_class = LoginForm

    def post(self,req,*args,**kwargs):
        form = self.form_class(data = req.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(req, username=username,password=password)

            if user is not None:
                login(req, user)
                redirect('/home')
            else:
                pass
        else:
            pass
            
    def get(self, req, *args, **kwargs):
        form = self.form_class()
        return render(req,'registration/login.html',{"form":form})


class SignUpView(View):
    form_class = SignUpForm

    def post(self,req,*args,**kwargs):
        form = self.form_class(data = req.POST)
        logout(req)
        if form.is_valid():
            user = User.objects.create_user(username=form.changed_data["username"],
                                            email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password"])
            login(req,user)
            return redirect('/home')
        else:
            
            #return redirect('/sign-up',"passwords are not same")
            pass

    def get(self, req, *args, **kwargs):
        print(*args)
        form = self.form_class()
        return render(req,'registration/sign_up.html',{"form":form})
