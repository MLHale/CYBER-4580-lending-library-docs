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
