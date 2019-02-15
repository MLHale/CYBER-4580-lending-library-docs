LITERATURE REVIEW



TECHNICAL PLAN
What we plan on doing is creating a backend with PostgreSQL with a front end of Django and Ember.js built on Docker. PostgreSQL is going to be used as our database to keep track of all the items that need to be tracked by the system as well as keep track of the users including their types: Borrowers, Lenders, and Admins. This will be our focus in the first few weeks, ensuring that the backend is functional and works as well as implementing several features such as creating logs for changes to the database. Through the front-end softwares Ember.js and Django the frontend will be brought to life, and create a site that is easy to navigate and secure from attacks like SQL injection, XSS, and other vulnerabilities to websites. For many of these vulnerabilities, Django comes with solutions to prevent these attacks. In addition, there will be a way for items to be added to lend by lenders. This is to make sure that the number of items can be added at any time. We plan for a base frontend to be done a few weeks after our backend, and then will spend several more weeks polishing it. 

We plan on testing our designs on a case by case basis but will try to include several vulnerabilities and attack vectors. For postgreSQL, testing will include testing the logging system as well as basic feature testing and *insert vulnerability here*. For Ember.js and Django, we plan on testing xss, sqlInjection and other vulnerabilities as well as basic functionality and user oriented changes. 
