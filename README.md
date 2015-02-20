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
3. Install dependencies and config the Django projectby setup script
``` bash
sudo python setup.py
```

## Running Django app
1. Run server
``` bash
python manage.py runserver
```
2. Launch web browser, enter correct IP address (Default is 127.0.0.1:8080) and your app is here.
