from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home', views.HomeView.as_view(), name = "home"),
    path('login', views.LoginView.as_view(), name='login'),
    path('sign-up',views.SignUpView.as_view(),name="sign-up"),
]