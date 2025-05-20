from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('',views.home ,name='home'),
    path('additem/',views.additem,name = 'additem'),
    path('<int:id>/',views.details,name='details'),
]