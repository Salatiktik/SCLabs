from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view(), name = "home"),
    path('login', views.LoginView.as_view(), name='login'),
    path('sign-up',views.SignUpView.as_view(),name="sign-up"),
    re_path(r'^session/(?P<session_id>\d+)/$', views.SessionView.as_view(), name='session'),    
    path('sessions',views.SessionsView.as_view(),name="sessions"),
]