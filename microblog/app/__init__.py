from flask import Flask # imports the Flask class from flask library


# Instantiate the Flask class and save in the variable app
app = Flask(__name__)

# The next line is a bit confusing. There are 2 entities named app.
# There is our app package, which is the directory this file lives in
# and there is the app variable, which is an instance of Flask we 
# created on line 5.
# Below we are talking about the app package, which will contain the
# script "routes"
from app import routes
