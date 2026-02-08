from django.urls import path
from accounts.views import *

app_name ='accounts'

urlpatterns = [
    path('login', login_view , name='loginacc'),
    path('logout', logout_view , name='logoutacc'),
    path('signup', signup_view , name='signupacc'),

]
