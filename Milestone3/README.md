# Progress Report 5/2/2019
## Overview
For milestone 3, we have enabled communication between the frontend and backend. A user may now login to the frontend, which retrieves their unique data. Furthermore, they may populate their cart and place an order.

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
