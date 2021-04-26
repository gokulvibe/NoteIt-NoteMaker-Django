# NoteIt-NoteMaker-Django
A cloud based notes making web application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gokulvibe/NoteIt-NoteMaker-Django.git
$ cd NoteIt-NoteMaker-Django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv venv
$ source venv/bin/activate #for linux
$ venv\Scripts\activate #for windows
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt 
```
Once `pip` has finished downloading the dependencies:

Apply migrations:
```sh
(venv)$ python manage.py migrate
``` 
Run the server:

```sh
(venv)$ python manage.py runserver
```


And navigate to `http://127.0.0.1:8000/`.

