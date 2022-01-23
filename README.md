# aqua_track
Local website for tacking aquarium data.

The goal of this project is to develop an easy-to-use interface for tracking aquarium parameters and stocking. 

## Setup
Initial development will occur on a Windows 10 PC. Steps and isntalls will follow that formula.

### Software Installs
Docker
- https://docs.docker.com/desktop/windows/install/

Git
- https://gitforwindows.org/


### Clone the project from git
```bash
git clone https://github.com/nick-rc/aqua_track.git
```

## Git control process
1.) Create new feature branch
```
git checkout -b new_branch
```
2.) Develop your feature
- Make sure to perform through unit testing.

3.) Rebase your feature onto the current main/master.
```
git rebase main
```
4.) Checkout the main/master branch.
```
git checkout main
```
4.) Merge branch into master repo
- I use --no-ff to clarify how branches are developed and introduced into master/main. (It looks good using 'Git Graph' on VS Code too.)
```
git merge --no-ff new_branch
```
5.) Tag new feature and delete branch
```
git branch -d new_branch
```

## Testing
General Testing of full site.
```bash
docker-compose run aqua_track python3 manage.py test && flake8
```

## Development Process
Process for developing the Django app and additional features.

### 1.) Project Directory Setup
### 1.1) Create the project in GitHub
Can skip using GitHub if desire is to make repo private or just not usign that service.
- Create the new development project in GitHub. 
- Select the preferred license and gitignore filetype

### 1.2) Setup Dockerfile and Docker-Compose
https://www.docker.com/
- Create or add Dockerfile
- Create or add docker-compose.yml file

### 1.3) Setup the Django project
- Setup Dockerfile for Linux and Project Setup
The following code sections are added to the Dockerfile to setup an ubuntu image and install pip

```bash
FROM ubuntu:20.04

...

RUN set -xe \
        && apt-get update \
        && apt-get -y install python3-pip
RUN pip install --upgrade pip
```
- Create Django Project with Django Admin
First, create a new folder in your dev folder with your app name.
(aqua_track for example.)

Run the following code to setup your django project.
```bash
docker-compose run aqua_track django-admin startproject aqua_track .
```
This creates the files for a base django project in your development directory.

Now you can test the Django site.
```bash
docker-compose up
```
Take a look at the site in your browser at http://localhost:8000/

### 1.4) Add Flake8 Support
Current setup is a specific version range however will be updated.
- Add flake8 to requirements.txt if not already there
- create new flake8 file in the aqua_track directory.

### 1.5) Setup Local Settings and Hide Secret Key
- Followed these steps to hide secret key:
    https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl
- Setup a local_settings.py file in the same directory as settings.py
- Import all settings from settings.py into local_settings.py
- Overwrite any variables or add as needed.

### 1.6) Setup initial Core app
- Run the following command to setup your first app. This one is called 'core'
```bash
docker-compose run aqua_track python3 manage.py startapp core
```
This command can be used to startup the remaining apps as needed. 

### 2.) User Management API Setup
- Create a test_admin.py file for superuser testing
- Add UserManager class and User class to Core models.py
    - UserManager pulls from BaseUserManager
    - Custom user model permits email as username
- Setup UserAdmin in admin.py
- Setup URL Path in urls.py (Main dir)
```python
path('api/user/', include('user.urls')),
```
- Add rest_framework to installed apps.

### 2.1) Postgresql Setup
- Add dependencies to dockerfile.
** Note - downgraded pysocpg2 to 2.8 due to this issue with 2.9
[link]https://stackoverflow.com/questions/68024060/assertionerror-database-connection-isnt-set-to-utc

### 3.) Aquarium App API Setup
1. Start the app via django
```bash
docker-compose run aqua_track python3 manage.py startapp aquarium
```
2. Setup the follwoing directory structure. 
- >aquarium
  - >migrations
  - >tests
    - test_models.py
  - apps.py
  - models.py
  - serializers.py
  - views.py
3. Update main app urls.py and settings.py
```python
urls.py
...
path('api/aquarium/', include('user.urls')),
```
   - Add 'aquarium' to INSTALLED_APPS in settings.py
4. Add tests to the tests folder
   - Usually the baseline tests are:
     - Test getting list of objects
     - Test getting object detail
     - Test creating objects
     - Test editing/updating objects
     - Test objects limited to user
     - Test API only accessible to users.
5. Update urls.py
6. Create serializer classes in serializer.py
7. Create views in views.py
8. Make migrations
9. Create Model
```bash
docker-compose run aqua_track python3 manage.py makemigrations
```