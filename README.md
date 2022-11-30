# django_introspection Package

Introspect your Django project models

## Install

`pip install -e git+https://github.com/Arnaud-B/django-introspection.git#egg=django-introspection`

## Usage

Put ```django_introspection``` in your settings

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


## File format

Example of information file


```json
{
  "models": 11,
  "collections": {
    "Permission": {
      "path": "django.contrib.auth.models",
      "verbose_name": "permission",
      "db_table": "auth_permission",
      "fields": {
        "id": "AutoField",
        "name": "CharField",
        "content_type": "ForeignKey",
        "codename": "CharField"
      },
      ...
    }
  }
}
```

## More informations

time estimated : ~2 hours

testing on 2 medium projects and one large project

in V0.2 : unit test on external projects