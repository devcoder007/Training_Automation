# Angular 8 / Django Rest Framework / JSON Web Token Authentication

This is a Training Automation app showing how to make API calls with Angular 8 and Django Rest Framework, including how to send authentication headers so API calls will function when logged in.

## What this repo contains

The following files are interesting:

* angular_django_cors - The Django project and main settings file
* microblog - An app within the project, containing the Django Rest Framework views and URL routing

## Requirements

You need the following to run this app:

* Python 3.5 or higher (Python 2.x is not supported by Django 2.x)

## Setup

Open a terminal at the repo root, and run the following:

```
cd Training_Automation

python manage.py runserver
```

Your app will be available at http://127.0.0.1:8000.

## Database

This project uses a SQLite database, which lives in the file `db.sqlite3`. SQLite3 support should be available out of the box on most modern operating systems. 

## Logging into the app

The database included in this repository contains two users. The following are their usernames and passwords, which you may use for testing:

- admin / admin
