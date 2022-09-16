## Goal of this test

Before getting started, receive our thanks for taking the time to complete this test and for your interest in bringing your skills and experience to UgoFresh.

This being said, there is "complete this test"… Indeed, this is merely a basic project that you may take into any direction you would like. The goal is to show off your skills and prove that you will be able to adapt to our technical stack.

We would like to see you work a bit on the backend (adding or extending or securing a WebAPI call, pagination, maybe adding some MQTT-WS messaging for live updates, unit tests, etc…) and a bit of work on the frontend (data visualisation, filtering, multiple selection for bulk actions, loading indicators, …). It is ok too to do some infrastructure work (adding authentication with a read-only anonymous mode, kubernetes configuration, adding a CouchDB/MongoDB datastore, …), or focus a bit more on technical documentation and code organisation.

I do not want this to be overwhealming or represent too much work. Please do not try to do *everything*. Let's keep this simple; I expect your work to be limited in scope. This being said, whatever work you do, should work well and be representative of your skills. Also, hopefully I wish you have fun doing this test. Yes, it is work, but hopefully it is as much your passion as it is ours and you can find .

It is very important to us that - as a coworker - you be able to say "I don't know", "I disagree, and here's why…", "I need help with…". We value autonomy but not solipsism. In that spirit, feel free to ask questions and communicate through out the *test*. 

## About this sample project

There are products. Products have a price, a category, and a name. Prices are historicized.
The initial project merely lists the products, their price, and category.

Minimally we would like to see :

  - the ability to update a product price,
  - the ability to group or degroup products by category,
  - price trend visualisation (bare minimum being a comparison to the last known value with a up/down/stable).


## Getting started

### With Docker

*Just* run the following command:

`docker build -t ugo:test .`
`docker run --rm -v "$(pwd):/code" -p "5000:80" ugo:test`

You may access `http://localhost:5000/` through your Web browser.

Note: the same project will rely on a sqlite3 backend. Feel free to use Docker Compose or another system to add a postgresql database.

### Without Docker

It is highly recommended that you rely on virtual environments. Depending on your operating system and python distribution, you may need to adapt the following commands:

  1. `python3 -m venv venv`
  2. `source ./venv/bin/activate`

Having activated your virtual environment, please install the dependencies:

  - `pip install -r requirements.txt`
  
And finally run the solution:

  - `python manage.py runserver 0.0.0.0:5000`

You may access `http://localhost:5000/` through your Web browser.

## Code Orientation

The base [Django project](https://www.djangoproject.com) is named `recruit`. It contains an *app* named `api` which serves some minimal REST-like APIs.

The *front* is served by the `recruit` project, as it is a single HTML/JS page.

That page uses [KnockoutJS](https://knockoutjs.com), but feel free to rebuild it using the framework of your choice (VueJS, React, …)

As such the main files to be aware of are:

  - `./recruit/urls.py`
  - `./recruit/views.py`
  - `./recruit/templates/index.html`
  - `./api/urls.py`
  - `./api/views.py`
  
The most important URLs:

  - `/api` : will list and let you explore the api calls
  - `/api/populate` : will reset the products with some random generation
  - `/` : a simple list of products
  - `/categories` : a slightly more involved example


## Good luck

We would be delighted if you could get back to us within the week so we can schedule a debrief session.
