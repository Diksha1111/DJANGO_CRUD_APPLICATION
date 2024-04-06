# DJANGO_CRUD_APPLICATION
This is a very simple Django project to demonstrate Django CRUD Application using Functional Based Views.
In this project user can  create,read,update and delete data.
![CRUD](https://github.com/Diksha1111/DJANGO_CRUD_APPLICATION/assets/89095400/0d838246-2f1b-4ffb-bd42-1adf7ec3ea1f)

STEP BY STEP GUIDE :
1. Download and install PYTHON
2. INSTALL VIRTUALENV  
   pip install virtualenv
3. CREATE VIRTUAL ENVIRONMENT 
   virtualenv venv
4. ACTIVATE VIRTUAL ENVIRONMENT
   venv\Scripts\activate
5. INSTALL DJANGO
   pip install django
6. TO CREATE NEW PROJECT
   django-admin startproject travel
7. TO CREATE NEW APP UNDER THAT PROJECT
   cd travel
   django-admin startapp ticket
8. OPEN settings.py FILE OF PROJECT(travel) , ADD APPNAME(ticket) under INSTALLED_APPS
9. OPEN urls.py FILE OF PROJECT(travel) , ADD path ('',include('ticket.urls'))
10. CREATE A NEW FILE urls.py INSIDE APP (add your path there)
11. CREATE TEMPLATES FOLDER INSIDE APP , create new file (index.html)
12. CREATE FOLDER STATIC INSIDE APP , create new file (style.css)
13. GO TO views.py OF APP (app your code)
14. GO TO models.py (create your class)
15. RUN YOUR PROJECT AND TEST IT
    
python manage.py makemigrations

python manage.py migrate

python manage.py runserver





