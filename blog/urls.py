
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('home' , BlogHome_view , name='homeblog'),
    path('single' , BlogSingle_view , name='singleblog'),
    
]