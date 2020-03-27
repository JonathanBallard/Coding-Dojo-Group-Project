import re
import json
from config import app, bcrypt, db
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from models import Users, FBUsers, Videos, Streams
from sqlalchemy.sql import func



#Login/Reg




#Videos Page




#Stream Page
# BLAH



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
    return render_template("create.html", thisUser = thisUser)


#Admin Page
@app.route("/admin")
def adminPage():
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    allUsers = Users.query.all()
    return render_template("admin.html", thisUser = thisUser)


#Edit User Page
@app.route("/editUser/<userID>")
def editUserPage(userID):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    userToEdit = Users.query.get(userID)
    return render_template("edituser.html", userToEdit = userToEdit, thisUser = thisUser)


#Update User POST Route
@app.route("/updateUser/<userID>", methods=["POST"])
def updateUser(userID):
    userToEdit = Users.query.get(userID)

    admin = request.form['admin']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    email = request.form['email']
    creatorName = request.form['creator_name']
    earningsTips = request.form['earnings_tips']
    earningsDonations = request.form['earnings_donations']
    earningsTimeBased = request.form['earnings_watcher_seconds']
    FBUserID = request.form['fb_user_id']

    userToEdit.admin = admin
    userToEdit.first_name = firstName
    userToEdit.last_name = lastName
    userToEdit.email = email
    userToEdit.creator_name = creatorName
    userToEdit.earnings_tips = earningsTips
    userToEdit.earnings_donations = earningsDonations
    userToEdit.earnings_watcher_seconds = earningsTimeBased
    userToEdit.fb_user_id = FBUserID

    db.session.add(userToEdit)
    db.session.commit()


    return redirect("/admin")


#Delete User Route
@app.route("/deleteUser/<userID>")
def deleteUser(userID):
    thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    userToEdit = Users.query.get(userID)
    if thisUser.admin == True:   #make sure person trying to delete this User is an admin
        db.session.delete(userToEdit)
        db.session.commit()
        return redirect("/admin")
    else:
        return redirect("/")



























if __name__ == "__main__":
    app.run(debug=True)

