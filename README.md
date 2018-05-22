# CARPOOL-R-US
## An application that allows users to share a ride / carpool from one place to another built using Django 1.11.


## By **[Samirah Maison](https://github.com/sami-mai)**

## Description
[This](https://mai-carpool.herokuapp.com/) A rendition of the website for the popular ride sharing app [Uber](https://www.uber.com/) built using Django 1.11.

## User Stories
###Rider User Story
* Sign in to the application to start using.
* Set up a profile about me and a general location.
* Find a list of drivers near me.
* View a map with the location of all pickup points.
* Review a driver and also be reviewed by the driver.
* View the current space left in a driver’s car and get to book It.

###Driver User Story
* Sign up as a driver to use the application
* Set up my drivers profile.
* View a map with the location of all pickup points.
* View all the requests for a ride.
* Review passengers coming on to your application.


## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd uberDjango`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE gram
```
9. Change the database information in `instaProject/settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uberdb',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
```
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application


## Known Bugs

No known bugs


## Technologies Used
- Python3.6
- Django
- Bootstrap
- Postgres Database
- CSS
- HTML
- Heroku

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
MIT (c) 2018 **[Samirah Maison](https://github.com/sami-mai)**

## Acknowledgements
* Moringa School
