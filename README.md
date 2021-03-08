# Articles

----
**Install project**

```
git clone https://github.com/Nikita-Filonov/articles.git
```

**Create virtual environment**

MacOS
______

``` 
mkdir environments

cd environments

python3 -m venv selenium_env

source selenium_env/bin/activate
``` 

Ubuntu
______

``` 
sudo apt-get update && sudo apt-get upgrade

sudo apt-get install python3.7

python3 -m pip install pip

sudo apt-get install -y python3.7-venv

mkdir environments

cd environments

python3 -m venv selenium_env

source selenium_env/bin/activate
``` 

Windows
______

``` 
mkdir environments

cd environments

python -m venv selenium_env

selenium_env\Scripts\activate.bat
```

**Install requirements**

```
pip install -r requirements.txt
```

Apply migrations

```
python manage.py makemigrations 

python manage.py migrate
```

Run server

```
python manage.py runserver
```

Look at `http://127.0.0.1:8000/login/`
