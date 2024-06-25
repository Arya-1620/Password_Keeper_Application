# C:\Users\arya\Documents\Python Projects\Password-Keeper\passwordkeeper\passwordkeeper_app\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add/', views.add_view, name='add'),
    path('decrypt/<int:id>/', views.decrypt_view, name='decrypt'),
]
