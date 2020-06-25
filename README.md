# django-json

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Thanks for checking it out.

Quick steps to go through of this repo to work.

Packages to me installed are:
  python,
  django,
  djangorestframework,
  djangorestframework-jsonapi,
  django-filter.
  
Create a project called django-jsonapi.

Create an application called activity.

Setup the INSTALLED_APPS, REST_FRAMEWORK and DATABASES in settings.py.

Create models in models.py:
  User,
  ActivityPeriod.

Setup serializers.py which translate models to their end-user-facing format.

Implement views.py to server in the json format.

Create endpoints in UPIs.
