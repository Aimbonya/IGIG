from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    SITE_EMPLOYEE = 'site_employee'
    EMPLOYEE = 'employee'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (SITE_EMPLOYEE, 'Site Employee'),
        (EMPLOYEE, 'Employee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ForeignKey, not unique

    def __str__(self):
        return f"Review by {self.name}"

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    duration = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)
    tickets_sold = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    ticket_cost = models.FloatField(default=5)

    def __str__(self):
        return self.name


class Showtime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.movie.title} in {self.hall.name} on {self.datetime}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(upload_to='posters/', default='photo_2022-12-25_17-03-47.jpg')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class TicketSale(models.Model):
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    sale_datetime = models.DateTimeField(auto_now_add=True)
    ticket_count = models.IntegerField()

    def __str__(self):
        return f"{self.ticket_count} tickets sold by {self.employee.name}"


class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=500)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', default=None)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Term(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term


class Contact(models.Model):
    photo = models.ImageField(upload_to='contacts/')
    name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    free_positions_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PromoCode(models.Model):
    code = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    discount = models.FloatField(default=1.0, validators=[MinValueValidator(0.0), MaxValueValidator(1.0)])

    def __str__(self):
        return self.code


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


