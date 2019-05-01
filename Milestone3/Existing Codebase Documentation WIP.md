# Existing Codebase Documentation
This file is used to document the existing codebase for future use. It will include useful files and their description so that
anyone that uses/continues this project later on will have an easier time understanding what files were included and why

## Backend
Filepath | Description
---------|-------------
api > admin.py | this file contains the models that can be added by the admins.
api > controllers.py | Holds viewsets, Registration, and session forms
api > models.py  | this file contains the database models that are being used by the application.  
api > urls.py | Contains the "router" and routes used by the front end.
README.md | Basic Readme file for the project. Includes information on the project itself and licensing information.
.gitignore | Incldues files that do not need to be committed to Github.

## Frontend
Filepath | Description
---------|-------------
app > components > cart-view.js | used to handle actions on the cart page including emptying and checking out items from a cart
app > controllers > library.js | holds code responsible for adding items to a cart
app > initializers > auth-manager.js | initializes the auth-manager code in given sections of the application
app > models | this folder contains all of the models used by the front end
app > routes | contains all of the routes for the front end
app > services > auth-manager.js | Contains the code for session management including login and logout
app > templates | contains all of the handlebars (.hbs) files used for the frontend
app > router.js | this file contains all of the routes that get presented in the menu bar on the frontend
public > assets | this folder contains all of the image assets used by the frontend.


## Component Specific Files
Components | Files
---------|-------------
Database | Models.py
Login | auth-manager.js, controllers.py, 
Cart | 
Order |

## To Do
Backend > API > controllers.py, urls.py
Backend > DjangoBackend > Localsettings.py, settings.py, urls.py, wsgi.py

## Verison History
 Date | Editor | Description
------------|--------|-------------
4/30/2019 | Jacob Levy | Added entries for the frontend files as well as Cart and Login components
4/18/2019 | Jacob Levy | Added Component section and entry for the database, login component, added frontend entries: urls.py, controllers.py, 
3/27/2019 | Jacob Levy | Added the To Do Section, and Readme and gitignore files in the backend.
3/26/2018 | Jacob Levy | Created document. Added Title and brief document description, backend title and documentation and frontend title.
