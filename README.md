# django-introspection Package

Introspect your Django project models

## Install

`pip install -e git+https://github.com/Arnaud-B/django-introspection.git#egg=django-introspection`

## Usage

Put ```introspection``` in your settings

   ```python
  INSTALLED_APPS = [
       'django_introspection',
       
       'django.contrib.auth',
       'django.contrib.contenttypes',
  ] 
  ```

Put in your wsgi.py file

   ```python
   from django_introspection import introspection
   introspection()
  ```

And you get file contains your models and attributes in your project root
