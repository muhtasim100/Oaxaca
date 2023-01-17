from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #need to query database and verify
        #and add according links to the required pages or flashes if something is incorrect
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"
    #need to link back

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #error checking
        if len(email) < 4:
            flash("Email must be greater than 4 characters", category='error')
        elif len(firstName) < 2:
            flash("First name must be greater than 2 characters", category='error')
        elif password1 != password2:
            flash("Passwords must match", category='error')
        else:
            #add user to database
            pass
    return render_template("signup.html")
