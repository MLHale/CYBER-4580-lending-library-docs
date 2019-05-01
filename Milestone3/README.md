# Progress Report 5/2/2019
## Overview
Working towards completing our objectives has produced both successes and significant challenges. After reviewing the feedback from our Milestone 2 results, we decided to commit more of our team's resources to focused tasks and more effective dissemination of work. Specifically, we had been pausing our work on the frontend deliverables in order to focus more on just the backend and at the onset of Milestone 3 this changed. The team broke apart into individual and separate focus areas: finishing the backend, working on the frontend, further documentation, and security evaluation.

We now have enabled communication between the frontend and backend. A user may now login to the frontend, which retrieves their unique data. Furthermore, they may populate their cart and place an order.

## Outcomes
User may:
* login to the website
* place items into their cart by itemtype and quantity
* place items into their cart by adding a package containing a group of itemtypes and respective quantities
* remove individual itemtype-quantities from their cart
* empty their cart
* place an order if sufficient items exist

## Hinderances
* Lazy-loading of Ember Store records caused difficulty when attempting to console.log() values. Usage of Ember observers is necessary to override this behavior.
* Backend code involving models, serializers, and viewsets required considerable modifications to successfully communicate with the frontend.
* Made mistakes regarding the use of singular and plural names for serializer includes.
* Third-party reference examples sometimes used varied syntax.
* Object-level permissions have proven difficult to implement
