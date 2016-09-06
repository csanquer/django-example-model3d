Django project Example
======================

Requirements
------------

* postgresql 9
* Python 3
* Python pip packages
  * Django
  * Pyaml

You can use [this docker config](https://github.com/csanquer/django-docker) to run the application

Install
-----

1. Copy `sketchfab/settings.py.dist` to `sketchfab/settings.py` and edit the environment values (e.g. : database settings)

2. Create a database

3. run django migration

```sh
python manage.py makemigrations
python manage.py migrate
```

4. load initial data

```sh
python manage.py loaddata data.yaml
```

5. run development server on a specified port

```sh
# run on port 8000
python manage.py runserver 0.0.0.0:8000
```
