Password Keeper Application:

Objective:Create a an application to keep all the important passwords

```Commands required:
    virtualenv venv #creating the virtual env
    \venv\Scripts\activate
    pip install django
    django-admin startproject passwordkeeeper
    python manage.py runserver
    pip install cryptography
    pip freeze>requirement.txt
    pip install -r requirement.txt
    django-admin startapp passwordkeeeper_app
    ```
Testing decrypting and encrypting function:
python manage.py shell
from passwordkeeper_app.views import encrypt_string, decrypt_string

encrypted_text = encrypt_string('hello')
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt_string(encrypted_text)
print(f"Decrypted text: {decrypted_text}")```
    
