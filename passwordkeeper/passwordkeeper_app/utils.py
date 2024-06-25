from django.conf import settings
from cryptography.fernet import Fernet
from .models import Password

def get_cipher_suite():
    key = settings.PASSWORD_SECRET_KEY
    cipher_suite = Fernet(key.encode())
    return cipher_suite

def encrypt_string(plain_text):
    cipher_suite = get_cipher_suite()
    encoded_text = cipher_suite.encrypt(plain_text.encode('utf8'))
    return encoded_text.decode()

def decrypt_string(encoded_text):
    cipher_suite = get_cipher_suite()
    decoded_text = cipher_suite.decrypt(encoded_text.encode('utf8')).decode()
    return decoded_text
