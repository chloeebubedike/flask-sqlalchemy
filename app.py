from application import app
from flask import Flask
# import the ./application/routes.py file
from application import routes




if __name__ == '__main__':
     # app.run(debug=True, host='0.0.0.0')
     app.run(debug=True, port=5010)


     # mvc Model View Controller
     # Separation of concerns
     # Templates - visual, presentation, UI : VIEWS
     # routes.py - CONTROLLER, flow
     # MODEL: data, CRUD: Create Read Update Delete
     # SQL analogy, CRUD: Insert, Select, Update, Delete