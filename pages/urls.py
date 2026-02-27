from django.urls import path 
from . import views


urlpatterns = [
    path("", views.home, name="home"), # homepage for 0.0.0.0:8000
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path('users/<int:id>/', views.user_profile, name='user_profile'),
    path('books/', views.book_list, name='book_list'),
    path('books/search/', views.book_search, name='book_search'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),

]