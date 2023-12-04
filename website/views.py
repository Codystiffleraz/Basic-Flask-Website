from flask import Blueprint, render_template

# Set up a blueprint 
views = Blueprint('views', __name__)

# Main page of website, whatever is in there is going to run
@views.route('/')
def home():
    return render_template("home.html")