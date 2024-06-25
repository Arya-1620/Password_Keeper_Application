# C:\Users\arya\Documents\Python Projects\Password-Keeper\passwordkeeper\urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('passwordkeeper_app/', include('passwordkeeper_app.urls')),  # Include the app's urls
]
