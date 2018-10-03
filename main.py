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
    password_verify = request.form['verify']
    email = request.form['email']

    field_blank = is_blank(username, password, password_verify)
    #password_valid

    template = jinja_env.get_template('signup.html')
    if field_blank == False:
        return template.render(username=username,email=email)
    else:
        return template.render(username_error="error: field blank")

def is_blank(usr, pw, v_pw):
    if usr == "" or pw == "" or v_pw == "":
        return True
    else:
        return False

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render(username="",email="")

app.run()