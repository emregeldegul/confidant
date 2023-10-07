# Confidant
Confidant is a simple web application that allows the diary to be stored on the web. Confidant has been and continues to be developed with Flask.

## Installation
Installation requires Python3 and Virtualenv.

```bash
~$ git clone https://github.com/emregeldegul/confidant.git && cd confidant
~$ python3 -m virtualenv venv
~$ source venv/bin/activate
~$ pip install -r requirements.txt
~$ flask db upgrade
~$ flask run
```

Please visit the address with a web browser.

Confidant URL: http://127.0.0.1:5000/

And login by creating a membership.

## To Do
- [x] Multi User
- [x] Editing Profile / Password
- [x] Saving Diaries with Encryption


## Used Technologies
* [flask] - Micro web framework
* [flask-sqlalchemy] - An extension for Flask that adds support for SQLAlchemy to your application.
* [flask-bcrypt] - Flask extension that provides bcrypt hashing utilities for your application.
* [flask-login] - Provides user session management for Flask.
* [flask-wtf] - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
* [bootstrap] -  For fast and responsive front-end design.
* [datatables] - Advanced table controls.


[flask]: <http://flask.pocoo.org>
[flask-sqlalchemy]: <https://flask-sqlalchemy.palletsprojects.com/en/2.x>
[flask-bcrypt]: <https://flask-bcrypt.readthedocs.io/en/latest>
[flask-login]: <https://flask-login.readthedocs.io/en/latest>
[flask-wtf]: <https://flask-wtf.readthedocs.io/en/stable>
[bootstrap]: <https://getbootstrap.com/>
[datatables]: <https://datatables.net/>
