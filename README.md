To Do Tasks
===========


### Introduction
To do tasks is normal to do lists with extra feature of tasks getting refreshed everyday i.e even after you tick off a task it gets unticked next day. The main advantage is it helps you keep track of the daily mandatory tasks and keep you aware of what is completed each day. This comes under daily tasks section. There is one more section called general tasks section which is similar to normal to do checklist. 

---

#### Features
- Application is a role based application. Admins can manage the users and grant admin access. Admins can see the feedback given by the users as well.
- Two sections are present in To Do tasks
    - Daily Tasks (gets refreshed everyday)
    - General Tasks
- Tasks can be checked/ticked and unchecked/unticked.
- We can delete the tasks from ticked and unticked as well.
    - Note: Tasks under daily tasks should be deleted if you don't want a task to be refreshed again next day.

---

#### Technical features
- Application is divided into three microservices
    - todo-lists (current one)
        - Maintains the tasks of the users and admins
    - todo-auth
        - Authentication server (More info check the repo)
    - todo-ui
        - User Interface (More info check the repo)
- Current Application (todo-lists)
    - Application is built using Python Flask Framework. Database is MongoDB
    - Since the database used is MongoDB (the tasks are not consistent and for array-based structure document-based database suits).
        - Querying of database happens using the name of the individual (decoded from access token)
    - User verification is done by decoding the JWT token (httponly access token).
        - The token is kept as a cookie in the browser by the authentication server and the frontend cannot access it.
    - The APIs are categorized into daily_tasks and general_tasks APIs.
    - Secrets are provided as environmental variables.
    - Application is dockerized to provide container based approach.
        - Application which can be deployed and can be scaled easily.
- Environment Variables to be provided before you run the application. (Either in dockerfile or docker-compose.yml)
    - SECRET_KEY
    - DATABASE_NAME
    - DATABASE_HOST
    - DATABASE_PORT
    - DATABASE_URL
    - FLASK_ENV
    - FLASK_PORT
    - DAILY_COLLECTION
    - GENERAL_COLLECTION
    - ACCESS_TOKEN
- Local setup 
  - Install python.
  - `pip install -r requirements.txt`.
  - `python run.py`.
        - If you want it run on different port, please specify as the environmental variable in the name of FLASK_PORT.
        - Add that in the User Interface as well.

---

#### Repo Links
- Authentication Server (todo-auth)
    - > https://github.com/sngrmvj/todo-auth
- User Interface (todo-ui)
    - > https://github.com/sngrmvj/todo-ui