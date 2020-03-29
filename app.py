import re
import json
from config import app, bcrypt, db
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from models import Users, FBUsers, Videos, Streams
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt

#Registration
@app.route("/")
def index():
    return render_template("login_reg.html")
    
#Login/Reg
@app.route("/register", methods=["POST"])
def registration():
    new_user = Users.add_new_user(request.form)
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    return redirect("/")

#Stream Page




#User Profile Page




#Stats Page
@app.route("/stats")
def statsRoute(userid):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    return render_template('stats.html', thisUser = thisUser)


#Create Page
@app.route("/create")
def createPage():
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    return render_template("create.html")


#Admin Page
@app.route("/admin")
def adminPage():
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    allUsers = Users.query.all()
    return render_template("admin.html")


#Edit User Page
@app.route("/editUser/<userID>")
def editUserPage(userID):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    editingUser = Users.query.get(userID)
    return render_template("edituser.html", editingUser = editingUser)


#Update User POST Route
@app.route("/updateUser/<userID>", methods=["POST"])
def updateUser(userID):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    editingUser = Users.query.get(userID)

    admin = request.form['admin']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    email = request.form['email']
    creatorName = request.form['creator_name']
    earningsTips = request.form['earnings_tips']
    earningsDonations = request.form['earnings_donations']
    earningsTimeBased = request.form['earnings_watcher_seconds']
    FBUserID = request.form['fb_user_id']

    editingUser.admin = admin
    editingUser.first_name = firstName
    editingUser.last_name = lastName
    editingUser.email = email
    editingUser.creator_name = creatorName
    editingUser.earnings_tips = earningsTips
    editingUser.earnings_donations = earningsDonations
    editingUser.earnings_watcher_seconds = earningsTimeBased
    editingUser.fb_user_id = FBUserID

    db.session.add(editingUser)
    db.session.commit()


    return redirect("/admin")


#Delete User Route
@app.route("/deleteUser/<userID>")
def deleteUser(userID):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    editingUser = Users.query.get(userID)
    if thisUser.admin == True:   #make sure person trying to do this is an admin
        db.session.delete(editingUser)
        db.session.commit()
        return redirect("/admin")
    else:
        return redirect("/")



























if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')

