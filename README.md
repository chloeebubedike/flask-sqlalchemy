# Sample Flask Application
This application is a sample Python Flask web app that uses Jinja templates and SQLAlchemy.

## Setup
Open MySQL Workbench and create a new database, called for example _flask_team_a_.

```sql
create database flask_team_a;
```

Edit the following line of code in **__init__.py** to the _user_, _password_ and _database_ you wish to use:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:password@localhost/flask_team_a"
```

Run **create.py** to drop, create and populate the database tables with initial data.

## Run
To start the Flask app, run **app.py**.

## Routes
Test the **/people** and **/cars** routes.

## Postman
Use Postman to test the PUT and POST routes and then expand the app to include forms to add and edit people and cars as necessary.