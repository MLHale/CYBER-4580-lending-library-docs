# Existing Codebase Documentation
This file is used to document the existing codebase for future use. It will include useful files and their description so that
anyone that uses/continues this project later on will have an easier time understanding what files were included and why

## Backend
Filepath | Description
---------|-------------
api/admin.py | this file contains the models that can be added by the admins.
api/controllers.py | Holds viewsets, Registration, and session forms
api/models.py  | this file contains the database models that are being used by the application.  
api/urls.py | Contains the "router" and routes used by the front end.
README.md | Basic Readme file for the project. Includes information on the project itself and licensing information.
.gitignore | Incldues files that do not need to be committed to Github.

## Frontend
Filepath | Description
---------|-------------
app/components/cart-view.js | used to handle actions on the cart page including emptying and checking out items from a cart
app/controllers/library.js | holds code responsible for adding items to a cart
app/initializers/auth-manager.js | injects the auth-manager service into all routes, controllers, and components as 'auth'
app/models/* | this folder contains all of the models used by the front end
app/routes/* | contains all of the routes for the front end
app/services/auth-manager.js | Contains the code for session management including login and logout. If login is successful, retrieves the userprofile, organization, cart, and cart contents
app/templates | contains all of the handlebars (.hbs) files used for the frontend
app/templates/login.hbs | Provides login fields and button for login action when user is not logged in. Also provides sign out button for logout action when user is logged in.
app/templates/components/cart-view.hbs | Displays cartitemtypequantities within the user's cart. Each cartitemtypequantity has a remove from cart button which performs the remove action on that specific record. Also has an empty cart button to perform the empty action to remove all cartitemtypequantities from cart. Place order button performs the order action which is based upon the cartitemtypequantities displayed on this page.
app/router.js | this file contains all of the routes that get presented in the menu bar on the frontend
app/routes/cart.js | Contains the model hook which returns all items and their associated itemtype relationships.
public/assets/* | this folder contains all of the image assets used by the frontend.


## Component Specific Files
Components | Files
---------|-------------
Database | Models.py
Login | app/services/auth-manager.js, app/initializers/auth-manager.js, controllers.py, login.hbs 
Cart | app/routes/cart.js, app/components/cart-view.js, app/templates/components/cart-view.hbs
Order |


## Verison History
 Date | Editor | Description
------------|--------|-------------
5/2/2019 | Jacob Levy | Added entries for more frontend files. Finished Login, Cart, and Order, component specific files; removed to do list
4/30/2019 | Jacob Levy | Added entries for the frontend files as well as Cart and Login components
4/18/2019 | Jacob Levy | Added Component section and entry for the database, login component, added frontend entries: urls.py, controllers.py, 
3/27/2019 | Jacob Levy | Added the To Do Section, and Readme and gitignore files in the backend.
3/26/2018 | Jacob Levy | Created document. Added Title and brief document description, backend title and documentation and frontend title.
