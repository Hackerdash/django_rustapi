from unicodedata import name
from task import views
from django.urls import  path

urlpatterns = [
    path('',views.home,name='home'),
    path('get',views.getdata,name='getdata'),
    path('postdata',views.postdata,name='postdata'),
]

