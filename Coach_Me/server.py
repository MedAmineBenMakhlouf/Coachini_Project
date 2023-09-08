from flask_app import app
from flask import Flask, render_template, request, redirect, url_for

# ! Don't forget to import all controllers here 
from flask_app.controllers import users,user_measures,programs,days,exercises,enrollings


if __name__ == '__main__':
    app.run(debug=True,port=5001)