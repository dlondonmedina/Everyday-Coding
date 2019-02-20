# the app package we created (this directory) has 
# the app instance of Flask in it in the __init__.py file.
from app import app 

@app.route('/')
@app.route('/index')
def index():
   return "Hello, World!"
   