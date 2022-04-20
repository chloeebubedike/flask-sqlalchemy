from flask import render_template, request
from application import app, db
from application.forms import BasicForm
from application.models import Person, Car


# get display info and post because taking in info (could use for view your courses and booking page)
# error message displayed if invalid values entered
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    # create empty variable for error message
    error = ""
    # save basic form class in the variable form
    form = BasicForm()

    # if the request method is post
    if request.method == 'POST':
        # save first name entered in the form in a variable
        first_name = form.first_name.data
        # save last name entered in the form in a variable
        last_name = form.last_name.data

        # if the length of the first or last name is zero show a prompt to tell the user to supply their names
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        # if the length of both of the names is above 0
        # create a person object with their details
        # add the person to the database
        # commit the change
        else:
            person = Person(first_name=first_name, last_name=last_name)
            db.session.add(person)
            db.session.commit()
            return 'Thank you!'

    return render_template('home.html', form=form, message=error)


@app.route('/people', methods=['GET'])
def show_people():
    error = ""
    people = Person.query.all()
    if len(people) == 0:
        error = "There are no people to display"
        print(people)
    return render_template('people.html', people=people, message=error)

# simple get (could use to display course info)
@app.route('/cars', methods=['GET'])
def show_cars():
    error = ""
    cars = Car.query.all()
    if len(cars) == 0:
        error = "There are no cars to display"
        print(cars)
    return render_template('cars.html', cars=cars, message=error, title="Car")


@app.route('/people/<int:person_id>', methods=['GET'])
def show_person(person_id):
    error = ""
    # use filter_by for any column
    # person = Person.query.filter_by(id=person_id).first()
    #  use get for the PK
    person = Person.query.get(person_id)

    # simpsons = Person.query.filter_by(last_name="simpson").all()

    # to sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).all()
    # descending sort
    # simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name.desc()).all()
    # limit to top 2 simpsons
    simpsons = Person.query.filter_by(last_name="simpson").order_by(Person.first_name).limit(2).all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=simpsons)


@app.route('/people/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = "Flanders"
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Person", family=[])


@app.route('/people/<int:person_id>/<string:new_last_name>', methods=['PUT'])
def update_person_with_name(person_id, new_last_name):
    error = ""
    person = Person.query.get(person_id)
    person.last_name = new_last_name
    db.session.commit()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
    return render_template('person.html', person=person, message=error, title="Updated Person", family=[])


@app.route('/people/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    error = ""
    person = Person.query.get(person_id)
    db.session.delete(person)
    db.session.commit()
    people = Person.query.all()
    if not person:
        error = "There is no person with ID: " + str(person_id)
        # print(person)
    return render_template('people.html', people=people, message=error, title="People")


# use to combine two different tables
@app.route('/personandcars/<int:person_id>', methods=['GET'])
def people_and_cars(person_id):
    error = ""
    person = Person.query.get(person_id)
    # cars= person.cars
    if not person:
        error = "There is no person with ID: " + str(person_id)
        print(person)
        # print(person_and_carinfo)
    return render_template('person_and_cars.html', person=person, message=error, title="Person and Car Info")

    # return render_template('home.html', form=form, message=error)