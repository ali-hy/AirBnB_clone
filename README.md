# AirBnB Clone

## Welcome to the AirBnB clone project

First step: Write a command interpreter to manage AirBnB objects.
This is the first step towards building a full web application: the AirBnB clone. This first step is very important because what is built during this project will be used with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

### The tasks in place expect the following

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What can the command interpreter do?

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
