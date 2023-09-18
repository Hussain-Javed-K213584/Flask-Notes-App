from flask import Blueprint, render_template, request, flash

# This file is a blueprint for our application

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return render_template('login.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password = request.form.get('password1')
        conf_password = request.form.get('password2')

        if '@' not in email:
            flash('Not a valid email.', category='failure')
        elif len(first_name) < 2:
            flash('Name too short.', category='failure')
        elif password != conf_password:
            flash('Passwords do not match.', category='failure')
        elif len(password) < 7:
            flash('Password should be atleat 7 characters.', category='failure')
        else:
            # Add user to database
            flash("Account created!", category='success')
    return render_template('sign_up.html')