# EXT_GEN

**EX**am **T**imetable **G**enerator is a Django app that aims at generating exam timetable automatically based on student record and available time slots.

This hopes to reduce the workload of teachers in scheduling exam timetable. It runs an optimization algorithm aimming at maximizing the revision time between subjects for students.

## Set up

1. Install dependencies by setup script
``` bash
sudo python setup.py
```
2. Clone into temp folder
``` bash
git clone https://github.com/cameronlai/EXT_GEN temp
```
3. Start Django Project
``` bash
django-admin startproject EXT_GEN_PROJECT
```
4. Copy Django app into project folder
``` bash
mv temp/* EXT_GEN_PROJECT/
```
5. Remove temp folder
``` bash
rm -rf temp
```

## Running Django app
1. Go to project folder
``` bash
cd EXT_GEN_PROJECT
```
2. Run server
``` bash
python manage.py runserver
```
3. Launch web browser, enter correct IP address and your app is here.
