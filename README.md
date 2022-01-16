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

'''bash
FROM ubuntu:20.04

...

RUN set -xe \
        && apt-get update \
        && apt-get -y install python3-pip
RUN pip install --upgrade pip
'''
- Create Django Project with Django Admin
Run the following code to setup your django project.
'''bash
docker-compose run aqua_track django-admin startproject aqua_track .
'''

### 1.4) Add Flake8 Support
Current setup is a specific version range however will be updated.
- Add flake8 to requirements.txt

