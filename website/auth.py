from flask import Blueprint, render_template

# Set up a blueprint 
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")