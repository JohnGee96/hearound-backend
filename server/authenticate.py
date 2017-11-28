from flask import Flask, abort, request, jsonify
from server.models import User, db
from server.app import app

@app.route('/api/signup', methods=['POST'])
def signup():
    if not request.json:
        abort(400, "Invalid Form")
    if all (key in request.json for key in ("email","password", "username")):
        if User.query.filter_by(email=request.json["email"]).first():
            abort(400, "Email address already exists")
        else:
            newUser = User(request.json["username"],request.json["email"], request.json["password"])
            db.session.add(newUser)
            db.session.commit()
            return "Sign Up Successful"
    else:
        abort(400, "Invalid Form")

def authenticate(json):
    input_email = json["email"]
    input_pw = json["password"]
    user = User.query.filter_by(email=input_email).first()
    if user:
        if user.checkPassword(input_pw):
            # print(user.password)
            return user.getUser()
    return None


@app.route('/api/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    if all (key in request.json for key in ("email","password")):
        user = authenticate(request.json)
        if user:
            return jsonify(user)
        else:
            return "Invalid Authentication"
    else:
        abort(400)