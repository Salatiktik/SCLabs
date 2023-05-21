import requests
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import LoginForm, SignUpForm
from .models import Session, Movie, Seat, SessionSeat
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import datetime
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
                render(req,'registration/login.html',{"form":form, "error":['Wrong username or password']})
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
            user = User.objects.create_user(username=form.cleaned_data["username"],
                                            email=form.cleaned_data["email"],
                                            password=form.cleaned_data["password"])
            login(req,user)
            return redirect('/home')
        else:            
            return render(req,'registration/sign_up.html',{"form":form,"error":form.errors.values})


    def get(self, req, *args, **kwargs):
        form = self.form_class()
        return render(req,'registration/sign_up.html',{"form":form})

class SessionsView(View):
    date = datetime.date.today()+datetime.timedelta(days=8)
    def get(self, req, *args, **kwargs):
        
        sessions = []
        sessionsFiltered = []
        for i in range(7):
            sessions.append(Session.objects.filter(startTime__gte=datetime.date.today()+datetime.timedelta(days=i+1),
                                          startTime__lte=datetime.date.today()+datetime.timedelta(days=i+2)).order_by('movie'))
            sessionsFiltered.append([])
            for j in range(len(sessions[i])):
                if j == 0:
                    sessionsFiltered[i].append([])
                    sessionsFiltered[i][0].append(sessions[i][0])
                    continue
                
                if(sessions[i][j].movie!=sessions[i][j-1].movie):
                    sessionsFiltered[i].append([])
                    sessionsFiltered[i][len(sessionsFiltered[i])-1].append(sessions[i][j])
                    continue

                sessionsFiltered[i][len(sessionsFiltered[i])-1].append(sessions[i][j])

        print(sessionsFiltered)

        return render(req,'cinema/sessions.html',{"sessions":sessionsFiltered})
    
class SessionView(View):
    def get(self, req, *args,session_id, **kwargs):
        session = Session.objects.get(id=session_id)
        hall = session.hall
        seats = Seat.objects.filter(hall=hall)
        sessionSeats = []
        for i in range(len(seats)):
            if(SessionSeat.objects.filter(session=session,seat=seats[i])):
                sessionSeats.append(SessionSeat.objects.get(session=session,seat=seats[i]))
        movie = session.movie
        print(movie.poster.url)
        return render(req,'cinema/session.html',{"session":session,"hall":hall,"seats":seats,"sessionSeats":sessionSeats,"movie":movie,"posterUrl":movie.poster.url})