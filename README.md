# EXT_GEN

**EX**am **T**imetable **G**enerator is a Django app that aims at generating exam timetable automatically based on student record and available time slots.

This hopes to reduce the workload of teachers in scheduling exam timetable. It runs an optimization algorithm aimming at maximizing the revision time between subjects for students.

## Set up

1. Start Django Project 

  ``` bash
  django-admin startproject EXT_GEN_PROJECT
  cd EXT_GEN_PROJECT
  ```

2. Clone the git repository

  ``` bash
  git clone https://github.com/cameronlai/EXT_GEN
  ```
    
3. Edit settings.py in your project folder. 
Note that older version of Django may require editting static files directories for loading css and js files

  ``` bash
  cd ../EXT_GEN_PROJECT
  nano settings.py
  ```

  > Add 'EXT_GEN' in INSTALLED_APPS

4. Edit urls.py in your project folder 
  
  ``` bash
  nano urls.py
  ```
  > Add url(r'^$', include('EXT_GEN.urls')), urlpatterns

5. Run migrations with manage.py

  ``` bash
  cd ../
  sudo python manage.py migrate
  ```

## Running Django app

1. Run server

  ``` bash
  python manage.py runserver
  ```

2. Launch web browser, enter correct IP address (Default is 127.0.0.1:8000) and your app is running.

## Dependencies

- Deap
- Numpy
- Tabulate

## License

The app is released under the MIT License and more information can be found in the LICENSE file.
