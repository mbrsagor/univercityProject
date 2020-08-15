# University Project

###### The project I'm developing for my university semester exam project.Implemented python popular web framework Django.

##### How to run the project locally?
> if you run or contribute the project please follow the requirements.

 - Python3.8
 - Virtual environment
 - Django 3.1
 
  
 You may download [python](https://python.org/) from here in your system.
 
 ```angular2html
git clone https://github.com/mbrsagor/univercityProject/tree/master
cd universityProject
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```