from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list_view, name='main_page'),
    path('book_list/', views.book_list_view, name='book_list'),
    path('image_django/', views.image_django_view, name='image_django'),
    path('about_me/', views.about_me_view, name='about'),
    path('contacts/', views.contacts, name='cont'),
]