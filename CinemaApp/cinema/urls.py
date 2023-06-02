from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('home/', views.HomeView.as_view(), name = "home"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign-up/',views.SignUpView.as_view(),name="sign-up"),
    path('sessions/',views.SessionsView.as_view(),name="sessions"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('movies/', views.MoviesView.as_view(), name='movies'),
    re_path(r'^session/(?P<session_id>\d+)/$', views.SessionView.as_view(), name='session'),
    re_path(r'^movie/(?P<movie_id>\d+)/$', views.MovieView.as_view(), name='movie'),
    re_path(r'^ticket_confirmation/(?P<session_id>\d+)_(?P<seat_id>\d+)/$', views.TicketView.as_view(), name='ticket_confirmation'),         
]

