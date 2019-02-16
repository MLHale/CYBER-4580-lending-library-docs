# Project Proposal for lending library  
### Team Members: Tareq Alomar, Cody Barrett, Jacob Levy, Nick Volenec  
February 15, 2019

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


### Timeline  
![Gnatt chart](https://github.com/nvolenec-uno/CYBER-4580-makerT1/blob/master/Proposal%20Stuff/Gantt%20Chart3.jpg)

### Risk list  
| Risk                          | Impact | Likelihood |
|-------------------------------|:------:|:----------:|
| Illness of team member(s)     |    4   |      4     |
| Lack of technical proficiency |    3   |      4     |
| Hardware Failure              |    5   |      2     |
| Inadequate Documentation      |    4   |      1     |
| Act of God                    |    8   |      1     | 

### Methodology  
#### Literature Review  
Keywords: Django Security, Ember.js Security, postgreSQL security, tech lending library, Web App Security, docker security  
Researching for information about the technology lending library, we found that Iowa State University has a Laptop and Equipment checkout which we could use for some ideas. When we looked into it we found a lot of it had to do with checkout times and when the items needed to be returned. Although according to our requirements we do not need to worry about lending dates as in-depth, we also were able to keep ideas in mind moving forward. Otherwise, a lot of the items we found involved security surrounding Django, Ember.js, postgreSQL, and docker security including patches, application security features, and how to secure web applications from attacks like SQL injection, Cross Site Scripting, and other common web application attacks.

#### Technical Plan 
Our plan is to develop a system with a PostgreSQL and Django back end and an Ember.js front end, built in a Docker container. PostgreSQL will be used to keep track of the inventory and it's state as well as users including their roles: Borrower, Lender, and Administrator. Django will be used to develop all server-side logic. Our front end will be in Ember.js, there will be a JSON API which will allow the Django back end to communicate with the Ember.js front end. The interfaces presented will be based on the roles assigned to the user.  A borrower will be presented with an interface that allows them to request items.  A lender will be presented with an interface that will allow them to fulfill requests from borrowers and also to add new items to the inventory.  An administrator will be able to add new borrower and lender users as well as manage inventory. A user may have multiple roles, a lender could also be an administrator. We will leverage Django’s built-in security features to create an application that is secure. We will test our design and the security of the system on an ongoing basis as the system is developed.

Our focus for the second milestone, ensuring that the back end is functional as well as implementing several features such as creating an activity log and which use performed them and an initial rough front end. Our focus for the third milestone will be completing any unfinished tasks from the second milestone, creating a polished front end, and if time permits working on our stretch goals of developing an interface that will allow new users to apply for a borrower account and the ability for items to be grouped into modules.

### Resource/Tech needed  
|  Resource  |  Dr. Hale Needed?  |  Investigating Team Member  |  Description  |
|------------|--------------------|-----------------------------|---------------|
|  Server Space  |  Yes  | Tareq | A domain name provided by Dr. Hale |
|  Docker  |  No  |  Nick  |  open-source application level container framework |
|  Django  |  No  |  Tareq/Nick  | open-source web framework based on Python |
|  PostgreSQL  |  No  |  Tareq  | Object-rational database management system for back-end |
|  Ember.JS  |  No  |  Tareq  | JavaScript framework for front-end |

#### User Stories
Borrower:
  Title: Be able to request an order from UNO Tech Lending Library.
Description:
  As a teacher in Omaha area, I need be able to request a package (via app), So that I can use UNO's resources.
Acceptance Criteria:
  - A list of items pop up when I click request.
  - When I select an item, I would be able to selcet the quantity.
  - When I select the quantity, I should be able to find the item(s) in my cart to check out.
  
Use Case: request an order
  - The use case begins when the user clicks "request"
  - The system responds by displaying item.
  - The user chooses the item & its quantity.
  - The system responds if the item is avaliable to lend them, put it into user's cart.
  -[Alt1] The user is ready to checkout.
  -[Alt2] The user wants to continue to order more items.
  - The user case ends when the user confirms to checkout all the requests. 
  
  
  Lender:
    Title: Be able to track an order that has been checked out by a teacher.
  Description:
    As a UNO faculity and staff, I need be able to track a package (via app), so I can keep monitor UNO's resources.
  Acceptance criteria:
    -Pending?
    -arrived?
    -search by an individual order to track? or see all the orders at once to track?
    -limitation time for lending?

### C4 diagrams
#### Level 1
<img alt="C4 Level 1 diagram" src="https://github.com/nvolenec-uno/CYBER-4580-makerT1/blob/master/Proposal%20Stuff/Level%201.jpeg" height="400" width="400">  

#### Level 2
<img alt="C4 Level 2 diagram" src="https://github.com/nvolenec-uno/CYBER-4580-makerT1/blob/master/Proposal%20Stuff/Level%202.jpeg" height="600" width="600">  


#### Level 3
![C4 Level 3 diagram](https://github.com/nvolenec-uno/CYBER-4580-makerT1/blob/master/Proposal%20Stuff/Level%203.jpeg)
