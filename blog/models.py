from django.db import models
from django.utils import timezone
from django import forms
from datetime import date
import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return "/blog/%i/" % self.id


class MojeModele(models.Model):
    przyklad = models.TextField(max_length=100, default="Przyladowy tekst")
    tekscik = models.TextField(max_length=20, help_text="Prosze podac przykladowy tekst")
    email_pole = models.EmailField(max_length=40, default="TwojAdres@email.com")

    published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    Piwo = 'Pi'
    Wodka = 'Wo'
    Wino = 'Wi'
    Shot = 'Sh'
    Drink = 'Dr'

    tabela_wyboru = [
        (Piwo, 'Piwo'),
        (Wodka,'Wodka'),
        (Wino,'Wino'),
        (Shot,'Shot'),
        (Drink,'Drink'),
    ]
    wybor = models.CharField(max_length=2, choices = tabela_wyboru, default="Wybierz napoj")

    liczba_calkowita = models.BigIntegerField(default=233)

    pole_wyboru = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    data_wpisu = models.DateField(auto_now=True)

    

    data_wpisu_2 = models.DateTimeField(auto_now=True)

    tresc_postu = models.TextField(default="Podaj tresc twojego postu.")

    tytul_postu = models.CharField(max_length=150,default="Podaj tytul twojego postu.")

    ilosc = models.DecimalField(max_digits=3, decimal_places=0, default=0)

    def __str__(self):
        return self.wybor
    def __str__(self):
        return self.tresc_postu
    def __str__(self):
        return self.tytul_postu

class Person(models.Model):
    Imie = models.CharField(max_length=200, default="Benedykt")
    Nazwisko = models.CharField(max_length=200, default="Kowalski")
    Wiek = models.IntegerField(default=18)
    
    def __str__(self):
        return self.Imie +" "+ self.Nazwisko

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                                   related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created', )

    def __str__(self):
        return 'Komentarz dodant przez {} dla posta {}'.format(self.name, self.post)
