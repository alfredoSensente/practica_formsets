"""library urls"""
from django.urls import path
from library import views

app_name = 'library'

urlpatterns = [
    path('home', views.authors_list, name='authors_list'),
    path('add_books/<int:id_author>', views.add_books, name='add_books'),
]
