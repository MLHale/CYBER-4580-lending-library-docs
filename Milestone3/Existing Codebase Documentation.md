# Existing Codebase Documentation
This file is used to document the existing codebase for future use. It will include useful files and their description so that
anyone that uses/continues this project later on will have an easier time understanding what files were included and why

## Backend
Filepath | Description
---------|-------------
api/admin.py | This file contains the models that can be added by the admins.
api/controllers.py | Holds viewsets, Registration, and session forms
api/models.py  | This file contains the database models that are being used by the application.  
api/urls.py | Contains the "router" and routes used by the front end.
README.md | Basic Readme file for the project. Includes information on the project itself and licensing information.
.gitignore | Incldues files that do not need to be committed to Github.

## Frontend
Filepath | Description
---------|-------------
app/components/cart-view.js | Used to handle actions on the cart page including emptying and checking out items from a cart
app/controller/library.js | Holds code responsible for adding items to a cart
app/controller/packages.js | Provides the add action for adding a package to the cart. Translates the data contained within the package/packageitemtypequantities into corresponding cartitemtypequantities for the user's cart.
app/initializers/auth-manager.js | Injects the auth-manager service into all routes, controllers, and components as 'auth'
app/models/* | This folder contains all of the models used by the front end
app/router.js | This file contains all of the routes that get presented in the menu bar on the frontend
app/routes/* | Contains all of the routes for the front end
app/routes/cart.js | Contains the model hook which returns all items and their associated itemtype relationships.
app/routes/packages.js | Contains the model hook which returns all packages and associated packageitemtypequantities.
app/services/auth-manager.js | Contains the code for session management including login and logout. If login is successful, retrieves the userprofile, organization, cart, and cart contents
app/templates | Contains all of the handlebars (.hbs) files used for the frontend
app/templates/login.hbs | Provides login fields and button for login action when user is not logged in. Also provides sign out button for logout action when user is logged in.
app/templates/packages.hbs | Displays created packages and provides the add to cart button to perform the add action.
app/templates/components/cart-view.hbs | Displays cartitemtypequantities within the user's cart. Each cartitemtypequantity has a remove from cart button which performs the remove action on that specific record. Also has an empty cart button to perform the empty action to remove all cartitemtypequantities from cart. Place order button performs the order action which is based upon the cartitemtypequantities displayed on this page.
public/assets/* | This folder contains all of the image assets used by the frontend.


## Component Specific Files
Components | Files
---------|-------------
Database | Models.py
Login | app/services/auth-manager.js, app/initializers/auth-manager.js, controllers.py, login.hbs 
Cart | app/routes/cart.js, app/components/cart-view.js, app/templates/components/cart-view.hbs
Package | app/routes/packages.js, app/controller/packages.js, app/templates/packages.hbs


## Verison History
 Date | Editor | Author|Description
------------|--------|----|---------
5/2/2019 | Jacob Levy | Jacob Levy, Nick Harper | Added entries for more frontend files. Finished Login, Cart, and Package, component specific files; removed to do list
4/30/2019 | Jacob Levy | Jacob Levy | Added entries for the frontend files as well as Cart and Login components
4/18/2019 | Jacob Levy | Jacob Levy | Added Component section and entry for the database, login component, added frontend entries: urls.py, controllers.py 
3/27/2019 | Jacob Levy | Jacob Levy |Added the To Do Section, and Readme and gitignore files in the backend.
3/26/2018 | Jacob Levy | Jacob Levy | Created document. Added Title and brief document description, backend title and documentation and frontend title.
