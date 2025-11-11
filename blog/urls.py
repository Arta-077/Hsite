
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('home' , BlogHome_view , name='homeblog'),
    path('<int:pid>' , BlogSingle_view , name='singleblog'),
    # path('<int:pid>' , test_view , name='testblog'),
    
]