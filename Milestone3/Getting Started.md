# Lending Library App Build Repository - Installation & Startup Instructions
These are the instructions to build the app for production mode. In its current state, the frontend must be built and placed in a folder within the backend, so it has a few dependencies in addition to Docker.

## Requirements
This app is containerized using Docker:
* Docker (https://docs.docker.com/install/)
* For Windows we used Docker Toolbox: https://docs.docker.com/toolbox/
However, the download no longer appears to be available on the docker website. It reads, "Docker Toolbox is now considered Legacy."

The following is needed to build the frontend:
* node
* npm
* bower
* ember-cli

### First Time Installing/Configuring Docker Toolbox
* Install Docker Toolbox
* Run the Docker Quickstart Terminal
* Open VirtualBox after it has finished initializing
* Right click on the VM it created called "default"
* Select Network from the menus on the left of the settings pop-up menu
* Click "advanced" to expand the menu
* Click Port Forwarding
* Add a new rule
* Name it "Lending Library" or something else relevant
* Set the Host Port to 8000 and the Guest Port to 80, and set the Host IP to the desired address. For development purposes we used localhost or "127.0.0.1"

## API (Backend) Installation
You need to build the docker image from the provided DockerFile using Docker Compose. To do this:

### Acquiring the files
```bash
git clone --recursive https://github.com/MLHale/lending-library-site-builds.git
cd lending-library-builds
git submodule sync
git submodule update --init --recursive --remote
```

### Update lending-library-backend/django_backend/localsettings.py
Change ENVIRONMENT from DEV to PROD, and insert the key for the SECRET_KEY field.

### Building and Running the API
While still in lending-library-builds folder:
```bash
docker-compose build
docker-compose up -d
```

This creates a few docker containers with all of the requisite installed dependencies to run the dev environment. It also initializes the database and starts the containers.

### Setup an Admin user and compile C libraries
To create a new admin user for use in the admin portal do the following once the containers are up and running (i.e. `docker-compose up -d` has been run). You can also use "run" in place of "exec" if the container is not running to perform the below command.

```bash
docker-compose exec django bash
python manage.py createsuperuser
# provide admin credentials
exit
```

### Building the Frontend and Placing it into the Backend
from `frontend`, run:
```bash
npm install
```
Some files may require bower, run the following if the prompt says bower is required:
(You may add the -g option to install globally, if desired)
```bash
npm install bower
```
The following will install dependencies that must be installed by bower:
```bash
bower install
```
npm may say that it has found vulnerabilities, run the following if it recommends to do so:
```bash
npm audit fix
```
Finally, build ember and send the output to the backend:
```bash
ember build --environment production -o ../lending-library-backend/static/ember
```

### Getting Started
The database will start out empty, so it must be populated before the app will function. Navigate to `localhost:8000/admin` and login with the credentials you provided in the steps where you created the superuser. The Django site administration portal will allow you to add records as needed. The project scope did not address creation and maintenance of records outside of this portal, so the app does not yet have this functionality.

Visit `localhost:8000` in your host browser when the database is populated to view the app in a usable form.

(Old Instructions:)
# Getting Started with the Lending Library

This guide assumes you are working in a Windows 10 environment.

### Things You'll Need
* Docker
* Git
* Chrome

### Process
* Install Docker Toolbox for Windows
  * It may ask that you allow VirtualBox to install also, this is required
  * Make sure Git is also installed in your Docker Toolbox
  * When the install is complete, open two instances of Docker Quickstart
    * One window should be used for the backend, and one for the frontend or dev commands.
* From your Docker Command Line
  * `git clone --recursive https://github.com/MLHale/lending-library-site-builds`
  * To work inside the proper branch:
    * `git checkout CYBER-4580-Spring2019` and then `git pull`
    * The checkout and pull commands should be run from both the `lending-library-frontend` and `lending-library-backend` folders.
    * To create your own branch off of ours:
      * `git checkout -b <your new branch name here>`
  * Change into the backend or dev directory if you aren't already there.
    * `docker-compose build` will create the Django database
  * Change into the frontend directory
    * `ember build -w -o ../lending-library-backend/static/ember`
      * This will likely fail the first time, and ask you to run additional commands such as `npm install` or `audit`, run the recommended commands and then run the `ember build` command again.
* Open VirtualBox
  * There should be a virtual machine running called `default`
  * In the settings area for `default`, click "Network", then "Advanced", then "Port Forwarding". Add a rule here with the "Guest Port" of 80 and "Host Port" of 8000.
* Open a Chrome tab
  * Docker typically uses 192.168.99.100 as it's default container IP, but it will list the IP it is using at the top of your Docker Quickstart window. Just scroll back to the top where the whale is drawn and you'll see what IP it is using.
  * In your Chrome tab, navigate to `<your Docker IP here>:8000` to see the site.
* Open a new instance of Docker Quickstart (don't close either of the other two).
  * Change directories into the backend folder.
  * Run `docker-compose exec django bash` to open a Django command line.
    * Run `python manage.py createsuperuser` to add an Administrative user to your database.
  * Back in your Chrome tab, navigate to `<your Docker IP here>:8000/admin/`.
  * Enter the username and password you created in the Django command line.
  * From this interface you can create new items, add users, manage permissions, etc.
