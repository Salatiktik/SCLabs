from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=20)
    genre = models.ManyToManyField(Genre)
    duration = models.TimeField()
    budget = models.FloatField()
    poster = models.ImageField()
    description = models.CharField(max_length=1000)
    rating = models.FloatField()
    trailerUrl = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=30)
    capacity = models.IntegerField()
    type = models.CharField(
        max_length=30,
        choices=(
            ('default', 'default'),
            ('IMAX', 'IMAX'),
        )
    )
    
    def __str__(self):
        return self.name


class SeatType(models.Model):
    type = models.CharField(max_length=10)
    rate = models.FloatField()
    
    def __str__(self):
        return self.type


class Seat(models.Model):
    hall = models.ForeignKey(
        Hall,
        on_delete=models.CASCADE,
        related_name="seats"
    )
    row = models.IntegerField()
    number = models.IntegerField()
    type = models.ForeignKey(
        SeatType, 
        on_delete=models.CASCADE, 
        related_name="types"
    )

    def __str__(self):
        return f"r{self.row}n{self.number}"

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    price = models.FloatField()
    type = models.CharField(
        max_length=30,
        choices=(
            ('3D', '3D'),
            ('2D', '2D'),
        )
    )

    def __str__(self):
        return f"{self.movie.__str__()}:{self.startTime}"


class SessionSeat(models.Model):
    is_occupied = models.BooleanField(default=False)
    seat = models.ForeignKey(Seat,  related_name="seats", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name="session_seats" ,on_delete=models.CASCADE)

class Ticket(models.Model):
    SessionSeat = models.OneToOneField(SessionSeat, related_name="ticket", on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    tickets = models.ManyToOneRel(Ticket,to=Ticket,field_name="tickets",related_name="user",on_delete=models.CASCADE)