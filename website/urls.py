
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('' , Home_view , name='index'),
    path('about' , About_view , name='about'),
    path('contact' , Contact_view , name='contact'),
    path('newsletter' , Newsletter_view , name='newsletter'),
    path('elements' , Elements_view , name='elements')
    
]