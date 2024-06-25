from django.shortcuts import render, redirect
from django.conf import settings
from cryptography.fernet import Fernet
from .models import Password
from .utils import get_cipher_suite,encrypt_string,decrypt_string



def index(request):
    password_list = Password.objects.all()
    return render(request, 'index.html', context={'password_list': password_list})

def add_view(request):
    if request.method == "POST":
        app_name = request.POST.get("appName")
        app_pass = request.POST.get("appPassword")
        Password.objects.create(
            name = app_name,
            password = encrypt_string(app_pass)
        )
        return redirect("/passwordkeeper_app/index")
    return render(request, 'index.html')  # Render the same template

def decrypt_view(request, id):
    password_obj = Password.objects.get(id=id)
    decrypted_password = decrypt_string(password_obj.password)
    password_list = Password.objects.all()
    return render(request, 'index.html', context={'password_list': password_list, 'decrypted_password': decrypted_password})