# Pizza

Am application for pizza store owners to managage their toppings and for pizza chefs to manage their pizzas.

## Dependencies 

asgiref==3.7.2

Django==5.0.2

django-debug-toolbar==4.3.0

sqlparse==0.4.4

tzdata==2024.1

## Local Installation

1. Clone the repository
```console
$ git clone https://github.com/sdevlin2/Pizza.git
```
2. Create your own virtual environment
```console
$ python3 -m venv venv
$ source venv/bin/activate
```


3. Install the requirements
```console
$ pip install -r requirements.txt
```

## Running


Start the server with:

```console
$ python manage.py runserver
```



Navigate to to http://127.0.0.1:8000/

## Running Tests Locally

Complete the local installation steps above, then run tests with:

```console
$ python manage.py test PizzaMaker
```
