# Django Cooking!

## Setting up a Python virtual environment

Through cmd, run

* pip install 
* cd DjangoCookbook
* pipenv install django==3.2.7
* pipenv shell

## Creating the project structure

Through cmd, run

* django-admin startproject DjangoCookbook . 

## Booting up the project

* python manage.py runserver

## Creating an app within the project

* python manage.py startapp pages
* Go to settings.py and add the app under INSTALLED_APPS

## Adding a view

* Add view logic inside of views.py
* Create a url.py file under the app (pages)
* Add the urlpatterns list structure and route the view to the url regex expression