from flask import Flask, request
import os
import cgi
import jinja2
import re


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    error_field_blank = "Error: Field blank"
    error_password_mismatch = "Error: Password Mismatch"
    error_password_invalid = "Error: Password Invalid"
    error_email_invalid = "Error: Invalid Email"
    error_username_invalid = "Error: Invalid Username"
    
    is_email_valid = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email)
    is_username_valid = re.match("^([a-zA-Z0-9@*#]{3,20})$",username)
    is_password_valid = re.match("^([a-zA-Z0-9@*#]{3,20})$",password)

    template_index = jinja_env.get_template('signup.html')
    if (is_email_valid == None and email != "") or is_username_valid == None or username == "" or is_password_valid == None or password != verify or password == "":
        return template_index.render(username = username, username_error = error_field_blank if username == "" else error_username_invalid if is_username_valid == None else "" , 
                                password = "", password_error = error_field_blank if password == "" else error_password_mismatch if password != verify else error_password_invalid if is_password_valid == None else "",
                                verify = "", verify_error = error_field_blank if verify == "" else error_password_mismatch if password != verify else error_password_invalid if is_password_valid == None else "",
                                email = email, email_error = "" if email == "" else error_email_invalid if is_email_valid == None else "")
    else:
        return "<h1>Welcome, {0}!".format(username)

@app.route("/")
def index():
    template_index = jinja_env.get_template('signup.html')
    return template_index.render()

app.run()