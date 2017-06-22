from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

usernamelist = ["", ""]

@app.route("/welcome", methods=['POST'])
def login():
    
    usererror = ""
    passerror = ""
    emailerror = ""
    verifyerror = ""

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    if (not username) or (username.strip() == "") or (" " in username) or (len(username) < 3) or (len(username) > 19):
        usererror = "That's not a valid username"
        usernamelist[0] = ""
    else:
        usernamelist[0] = username

    
    emaillist = list(email)
    
    if (email != "") and (("@" not in email) or (len(email) < 3) or (len(email) > 19) or ("." not in email) or (" " in email) or (emaillist.count(".") != 1)):
        emailerrorr = "Not a valid email"
        usernamelist[1] = ""
    else:
        usernamelist[1] = email

    if (not password) or (password.strip() == "") or (" " in password) or (len(password) < 3) or (len(password) > 19):
        passerror = "That's not a valid password"

    if(verify.strip() == "") or (password != verify):
        verifyerror = "Passwords don't match"
    
    
    if (usererror + passerror + emailerror + verifyerror != ""):
        return render_template('edit.html', username=usernamelist[0], email=usernamelist[1], usererror=usererror, passerror=passerror, verifyerror=verifyerror, emailerror=emailerror)

    usernameescaped = cgi.escape(username, quote=True)
    return render_template("welcome.html", username=usernameescaped)
    


@app.route("/")
def index():
    usererror = request.args.get("usererror")
    passerror = request.args.get("passerror")
    emailerror = request.args.get("emailerror")
    verifyerror = request.args.get("verifyerror")
    
    if usererror == None:
        usererror = ""
    if passerror == None:
        passerror = ""
    if emailerror == None:
        emailerror = ""
    if verifyerror == None:
        verifyerror = ""

    return render_template('edit.html', username=usernamelist[0], email=usernamelist[1], usererror=usererror, passerror=passerror, verifyerror=verifyerror, emailerror=emailerror)

app.run()
