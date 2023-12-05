# WORDCOUNT PROJECT

Learning Backend development with Django (Python), this is my first project.

From this project, I have learned
- How to pass data from forms into backend
- How to handle and manipulate data passed in by forms
- How to display manipulated data to the user in HTML
More to come.

## DJANGO - BACKEND DEVELOPMENT WITH PYTHON

A django project can contain an app or several apps (features of the project or pages of the app)

## CREATING A DJANGO PROJECT
1. ```django-admin startproject projectname``` is used to create a django project where projectname is the project's name
2. When the command and ran, it will create a directory with the name `projectname`.
3. Inside that directory, you'll find another directory with the same name as your project and a manage.py script.
4. The inner directory is where your project-specific settings, apps, and other project-related files will be stored. 
5. The manage.py script is used to manage various aspects of your Django project, such as running the development server, applying database migrations, and more.

## SETTING UP A VIRTUAL MACHING FOR DJANGO DEVELOPMENT
1. The tool `virtualenvwrapper` will help create a virtual space for your django project
2. To install `virtualenvwrapper` the command: ```pip install virtualenvwrapper```
3. To create a virtual environment, the command: ```mkvirtualenv env_name```
4. To show list of virtual enviroments on your system use command: ```workon```
5. To deactivate a virtual environment, use command: ```deactivate```
6. To activate a vitual environment, use command: ```workon env_name```

## GETTING STARTED WITH DJANGO PROJECT
After creating django project with ```django-admin startproject projectname```, you can create an app (page / feature) with:
1. Create an app with the command: ```python manage.py startapp myapp```
2. Add app to project, in settings.py
3. Define App's models inside `models.py`
4. Configure App's URLS inside `urls.py` file inside the app directory
5. Define Apps's views and templates
6. Run migrations to create database tables for the app
        commands
    ```
        python manage.py makemigrations myapp
        python manage.py migrate
    ```
7. Create superuser if the app has models that require administration
8. Add more apps if necessary
9. Run the project using command: ```python manage.py runserver```
