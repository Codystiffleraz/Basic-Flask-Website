from flask import Blueprint

# Set up a blueprint 
views = Blueprint('views', __name__)

# Main page of website, whatever is in there is going to run
@views.route('/')
def home():
    return "<h1>Test</h1>"