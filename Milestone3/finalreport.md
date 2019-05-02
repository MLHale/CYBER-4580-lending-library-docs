# Lending Library for IS&T

## Executive Summary
There is a technology lending library that teachers/instructors in the local area have access to. This is a great asset for the instructors who use it but in its current form is very difficult for both the instructors borrowing and the instructors lending. On the lending side, all the products are manually tracked and requests from borrowers have to be manually responded to. On the borrowers side, a request for a product is sent blindly, with no knowledge of whether or not the requested product will be available in the near future if at all, or whether the request was received by the right individual.

While our initial scope was to implement a system that could complete the item lifecycle, our results are limited to login, cart functionality, and order placement.

## Project Goals
Our goals/objectives are as follows:
* To automate the request process. Partially successful, orders may be placed and reviewed through the Django admin panel.
* To create a web application that will allow instructors to see what products are currently available. Partially successful, we did not fully meet this scope. However, the admin can see all items in the database via the Django admin panel.
* To allow lenders to track inventory. Partially successful, if an order is successfully placed, items allocated to that order will update to "Checked Out" status and will be assigned to the user who placed the order.

Our stretch goals/objectives are:
* To allow a new user to register via the web app. Unsuccessful, we did not meet this goal.
* To allow borrowers to place all items needed for a module into their "cart" in one click. Successful, we implemented package functionality, and multiple packages can be added to the cart at once.
* Successful completion of this project will allow instructors to more easily lend out and borrow products. This will result in more use of the library by its intended users and thus more effective education practices for the instructors utilizing the system.

## Project Methodology
### Literature Review
Keywords: Django Security, Ember.js Security, postgreSQL security, tech lending library, Web App Security, docker security.

Researching for information about the technology lending library, we found that Iowa State University has a Laptop and Equipment checkout which we could use for some ideas. When we looked into it we found a lot of it had to do with checkout times and when the items needed to be returned. Although according to our requirements we do not need to worry as much about lending dates, we were able to keep these ideas in mind moving forward. Otherwise, a lot of the items we found involved security surrounding Django, Ember.js, PostgreSQL, and Docker security including patches, application security features, and how to secure web applications from attacks like SQL injection, Cross Site Scripting, and other common web application attacks.

### Technical Plan
Our plan is to develop a system with a PostgreSQL and Django back end and an Ember.js front end, built in a Docker container. PostgreSQL will be used to keep track of the inventory and it's state as well as users including their roles: Borrower, Lender, and Administrator. Django will be used to develop all server-side logic. Our front end will be in Ember.js, and there will be a JSON API which will allow the Django back end to communicate with the Ember.js front end. The interfaces presented will be based on the roles assigned to the user. A borrower will be presented with an interface that allows them to request items. A lender will be presented with an interface that will allow them to fulfill requests from borrowers and also to add new items to the inventory. An administrator will be able to add new borrower and lender users as well as manage inventory. A user may have multiple roles, i.e. a lender could also be an administrator. We will leverage Django’s built-in security features to create an application that is secure. We will test our design and the security of the system on an ongoing basis as the system is developed.

Our development structure was as follows:
* Worked in weekly “Sprints” in which the team would work on items discussed at weekly meetings.
* At weekly meetings we would discuss progress made, issues encountered, and questions that were raised along with allowing for collaborative work to solve problems encountered.

For the second milestone, we focused on building our backend models and serializers.

For the third milestone, we mostly focused on essential frontend functionality. We adjusted the backend as necessary and developed login, cart, and order placement functionality. Time was also allocated towards input validation and user input response.

## Results / Findings

## Installation Instructions
