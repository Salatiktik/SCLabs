from django.contrib import admin
from .models import Movie,Genre,Hall,SeatType,Seat,Session,SessionSeat
# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Hall)
admin.site.register(SeatType)
admin.site.register(Seat)
admin.site.register(Session)
admin.site.register(SessionSeat)
