Lending Library project

slide 1

Project overview

The lending library project is an attempt to solve the following problem:
There exists a program where University of Nebraska personnel loan out equipment to local K-12 schools.  Currently this is an entirely manual process, requests are submitted via emailed and fulfilled manually by University of Nebraska personnel.
Our goal is to create a web interface that will streamline request, processing, and user management.



slide 2

Technology

Our solution will be built in a Django-Ember environment built on top of Docker with a PostgreSQL backend.

Docker is a platform for operating system leve virutalization

Django is an open-source python based framework for rapid web development

Ember is an open-source javascript framework

PostgreSQL is an open-source Relational Database system


slide 3

Security

Since this is a cybersecurity capstone project, one of our focuses is to create a system with robust secured.  
An initial list of security features we intend to implement:

-CSRF tokens on all forms
-A strict Content Security Policy to prevent code injection
-All SQL queries will be built using prepared statements
-Strong password policy
-Robust access/activity logging
-The JSON interface between the Django and Ember layers must be inaccessible to outside users
