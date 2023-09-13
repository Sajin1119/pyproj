from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.handleBlog,name='blog'),
    path('intenshipdetails',views.intenshipdetails,name='intenshipdetails')

]