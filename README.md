# Technology Lending Library

### Executive Summary
There is a technology lending library that teachers/instructors in the local area have access to. This is a great asset for the instructors who use it but in its current form is very difficult for both the instructors borrowing and the instructors lending. On the lending side, all the products are manually tracked and requests from borrowers have to be manually responded to. On the borrowers side, a request for a product is sent blindly, with no knowledge of whether or not the requested product will be available in the near future if at all, or whether the request was received by the right individual. 

Our goals/objectives are as follows:

* To automate the request process.

* To create a web application that will allow instructors to see what products are currently available.

* To allow lenders to track inventory.

Our stretch goals/objectives are:

* To allow a new user to register via the web app.

* To allow borrowers to place all items needed for a module into their "cart" in one click.

Successful completion of this project will allow instructors to more easily lend out and borrow products. This will result in more use of the library by its intended users and thus more effective education practices for the instructors utilizing the system. 

### Proposed Project Timeline
![Our Gantt Chart](https://raw.githubusercontent.com/nvolenec-uno/CYBER-4580-makerT1/master/Proposal%20Stuff/Gantt%20Chart3.jpg)

### Risk List
| Risk                          | Impact | Likelihood |
|-------------------------------|:------:|:----------:|
| Illness of team member(s)     |    4   |      4     |
| Lack of technical proficiency |    3   |      4     |
| Hardware Failure              |    5   |      2     |
| Inadequate Documentation      |    4   |      1     |
| Act of God                    |    8   |      1     |

### Project Methodology
LITERATURE REVIEW  
Keywords: Django Security, Ember.js Security, postgreSQL security, tech lending library, Web App Security, docker security.
Researching for information about the technology lending library, we found that Iowa State University has a Laptop and Equipment checkout which we could use for some ideas. When we looked into it we found a lot of it had to do with checkout times and when the items needed to be returned. Although according to our requirements we do not need to worry as much about lending dates, we were able to keep these ideas in mind moving forward. Otherwise, a lot of the items we found involved security surrounding Django, Ember.js, PostgreSQL, and Docker security including patches, application security features, and how to secure web applications from attacks like SQL injection, Cross Site Scripting, and other common web application attacks.

TECHNICAL PLAN  
Our plan is to develop a system with a PostgreSQL and Django back end and an Ember.js front end, built in a Docker container. PostgreSQL will be used to keep track of the inventory and it's state as well as users including their roles: Borrower, Lender, and Administrator. Django will be used to develop all server-side logic. Our front end will be in Ember.js, and there will be a JSON API which will allow the Django back end to communicate with the Ember.js front end. The interfaces presented will be based on the roles assigned to the user.  A borrower will be presented with an interface that allows them to request items.  A lender will be presented with an interface that will allow them to fulfill requests from borrowers and also to add new items to the inventory.  An administrator will be able to add new borrower and lender users as well as manage inventory. A user may have multiple roles, i.e. a lender could also be an administrator. We will leverage Django’s built-in security features to create an application that is secure. We will test our design and the security of the system on an ongoing basis as the system is developed.

Our focus for the second milestone, ensuring that the back end is functional as well as implementing several features such as creating an activity log and which user performed each action, and an initial rough front end. Our focus for the third milestone will be completing any unfinished tasks from the second milestone, creating a polished front end, and if time permits working on our stretch goals of developing an interface that will allow new users to apply for a borrower account and the ability for items to be grouped into modules.

### Requirements
|  Resource  |  Dr. Hale Needed?  |  Investigating Team Member  |  Description  |
|------------|--------------------|-----------------------------|---------------|
|  Server Space  |  Yes  | Tareq | A domain name provided by Dr. Hale |
|  Docker  |  No  |  Nick  |  open-source application level container framework |
|  Django  |  No  |  Tareq/Nick  | open-source web framework based on Python |
|  PostgreSQL  |  No  |  Tareq  | Object-rational database management system for back-end |
|  Ember.JS  |  No  |  Tareq  | JavaScript framework for front-end |
