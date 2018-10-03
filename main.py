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

    f_blank = "Error: Field blank"
    password_mismatch = "Error: Password Mismatch"

    template = jinja_env.get_template('signup.html')
    return template.render(username=username, username_error=f_blank if username=="" else "", 
                            password="", password_error=f_blank if password=="" else password_mismatch if password!=verify else "",
                            verify="", verify_error=f_blank if verify=="" else password_mismatch if password!=verify else "",
                            email=email)

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()

app.run()