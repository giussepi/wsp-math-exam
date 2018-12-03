Math class exams
================

Simple exam app

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Build The Stack
---------------
    $ cd wsp-math-exam/

    $ export COMPOSE_FILE=local.yml
    
    $ docker-compose -f local.yml build


Run the Stack
-------------
    $ docker-compose up
    
    Or run it detached
    
    $ docker-compose up -d

    Now http://127.0.0.1:8000 is available to any user and http://127.0.0.1:8000/admin/ is available to admin user (teachers, see below how to create an admin user using createsuperuser)
    Browse the REST API on  http://127.0.0.1:8000/api/


Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

If you're using docker just prepend docker-compose run django, like this

    $ docker-compose run --rm django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    
    $ docker-compose run django coverage run -m pytest
    
    $ coverage html
    
    $ open htmlcov/index.html

Or just print the report

    $ coverage run -m pytest
    
    $ coverage result

If you're using docker just prepend docker-compose run django, like this

    $ docker-compose run django coverage run -m pytest


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
