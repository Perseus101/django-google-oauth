# Getting Started
First, you will need to copy config/settings/local.py.example to config/settings/local.py and fill in the data from the Google Cloud Platform project. Once you've done that, run the following commands to start the server:

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

In a new terminal:
```bash
$ source venv/bin/activate
$ python manage.py migrate
$ python manage.py createsuperuser
```
After creating your super user, log into the [admin interface](http://localhost:8000/admin) and create a new `Application` with the following values:
* User: your super user
* Client Type: Public
* Authorization grant type: Resource owner password-based
* Name: Google OAuth2

Then, open you [application](http://localhost:8000/)!