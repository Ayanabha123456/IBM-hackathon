from django.urls import path

from . import views
app_name = 'COVID'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='register'),
    path('home/',views.home,name='home'),
    path('registered/',views.registered,name='registered'),
    path('logged/',views.logged,name='logged'),
    path('listed/<str:cat>',views.listed,name='listed'),
    path('add/',views.add,name='add'),
    path('cart/',views.cart,name='cart'),
    path('done/',views.done,name='done'),
]