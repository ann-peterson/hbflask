from flask import Flask, request, render_template
from random import choice, randint


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    """Say hello"""

    return "<html><body><h1>What's up friend?</h1></body></html>" #add code here to greet user

@app.route('/lucky')
def lucky_number():
    """Provides a random lucky number"""
    lucky_num = randint(1,1000)
    lucky_message = "Your lucky number is %s" % (lucky_num)

    # add code here of getting a lucky number and return a string
    # with the lucky number
    return "<html><body><h1>" + lucky_message + "</h1></body></html>"

@app.route('/template')
def define_template():
    return render_template("template.html")



if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
