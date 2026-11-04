
from django.shortcuts import render
from django.http import HttpResponse
from . import models
from datetime import datetime


def book_list_view(request):
    book = models.Book.objects.all()
    return render(request, 'book_list.html', {'book': book})


def image_django_view(request):
    return render(request, 'image_django.html')


def about_me_view(request):
    about_me = {
        "name": "Руслан",
        "work": "Официант",
        "hobby": "Чтение",
        "time": datetime.now(),
        "phone_numbers": ['0703648231', '0550789563']
    }
    return render(request, 'about_me.html', {'about_me': about_me})


def contacts(request):
    return render(request, 'contacts.html')
