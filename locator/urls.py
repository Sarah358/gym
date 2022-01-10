from django.urls import path
 
from . import views 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [ 
    path('', views.index, name='index'),
    path('gymdetails', views.gymdetails, name='gymdetails'), 
    path('packages', views.packages, name='packages'), 
    path('book', views.book, name="book"),
    path('bookings', views.bookings, name="bookings"),
    path('edit-book/<int:id>', views.edit_book, name="edit-book"),
    path('book-delete/<int:id>', views.delete_book, name="book-delete"),





     path('search-gyms', csrf_exempt(views.search_gyms),
        name="search_gyms"),

] 