# Remote offices API #

### Clonation of repository ###
$ git clone https://github.com/antobarbero/remote_offices_API.git

________________________________________________________________________


### How do I get set up? ###

Just run the following command for setup (Tested on Ubuntu 17.10)

```
$ sh setup_project.sh
```
* It will create a virtual environment, install the requirements and run the migrations.



#### Or manually follow these steps: ####


1. install python and python venv

```
$ sudo apt-get update

$ sudo apt-get install python3.6 -y

$ sudo apt-get install python3-venv -y

```

2.  create a virtual environment and activate it.

```
$ python3 -m venv .env

$ . .env/bin/activate
```


3. install the project requirements (with the virtual environment activated)

```
$ pip install -r requirements.txt
```

4. Run the database migrations

```
$ ./offices_API/manage.py migrate
```

________________________________________________________________________

### Activate python virtual environment ###

```
$ . .env/bin/activate
```
________________________________________________________________________

### Run the server ###

```
$ ./offices_API/manage.py runserver
```
________________________________________________________________________


### API documentation at home ###

http://127.0.0.1:8000

________________________________________________________________________

### How to run tests ###
```
$ ./offices_API/manage.py test offices_API
```

________________________________________________________________________

### Used libraries and frameworks ###

* Django==2.0.4
* djangorestframework==3.8.2
