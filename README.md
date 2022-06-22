# gudlift-registration
##

This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

## Features

- Python v3.x+
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need.
- [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)
  This ensures you'll be able to install the correct packages without interfering with Python on your machine.
  Before you begin, please ensure you have this installed globally. 


## Installation

 - After cloning, change into the directory and type <code>virtualenv .</code>. This will then set up a a virtual python environment within that directory.
 - Next, type <code>source bin/activate</code>. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>
- Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code>
- then go to the Gudlift folder
 - Flask requires that you set an environmental variable to the python file. To create the environmental variable for this project you need to do <code>$env:FLASK_APP = "server.py:createapp"</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details
- You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code> or <code>flask run --reload</code> or <code>python -m flask run --reload</code>. The app should respond with an address you should be able to go to using your browser.


## Current Setup

 The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
- competitions.json - list of competitions
- clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.


## Testing

this projest use [pytest](https://docs.pytest.org/en/7.1.x/)
and [locust](https://locust.io/)

- To run all test you need to be in the main folder and then enter the command <code>pytest</code>
- To run locust you need to go in the test folder and then run <code>locust</code> (the server need to be running)
