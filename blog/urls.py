
from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('home' , BlogHome_view , name='homeblog'),
    path('<int:pid>' , BlogSingle_view , name='singleblog'),
    path('category/<str:cat_name>' , BlogHome_view , name='categoryblog'),
    path('author/<str:author_username>' , BlogHome_view , name='authorblog'),
    path('search/' , BlogSearch_view , name='searchblog'),
    # path('<int:pid>' , test_view , name='testblog'),
    
]