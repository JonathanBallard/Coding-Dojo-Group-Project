import re
import json
from config import app, bcrypt, db
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from models import Users, FBUsers, Videos, Streams
from sqlalchemy.sql import func
from flask_bcrypt import Bcrypt


#Login/Reg
@app.route("/register", methods=["POST"])
def registration():
    new_user = Users.add_new_user(request.form)
    print(new_user)
    return redirect("/index")


#Videos Page




#Stream Page
# BLAH



#User Profile Page




#Stats Page
@app.route("/stats/<userid>")
def statsRoute(userid):
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
        return render_template('stats.html', thisUser = thisUser)
    else:
        testUser = Users.query.get(1) #TEST USER ID
        return render_template('stats.html', thisUser = testUser)
    


#Create Page
@app.route("/create")
def createPage():
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
        return render_template('create.html', thisUser = thisUser)
    else:
        testUser = Users.query.get(1) #TEST USER ID
        return render_template('create.html', thisUser = testUser)


#Admin Page
@app.route("/admin")
def adminPage():
    # testUser = Users(first_name = "NOT", last_name = "A", email = "USER", admin = False, creator_name = "testcase", description = "description")
    # db.session.add(testUser)
    # db.session.commit()
    allUsers = Users.query.all()
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
        return render_template('admin.html', thisUser = thisUser, allUsers = allUsers)
    else:
        testUser = Users.query.get(1) #TEST USER ID
        return render_template('admin.html', thisUser = testUser, allUsers = allUsers)


#Edit User Page
@app.route("/editUser/<userID>")
def editUserPage(userID):
    userToEdit = Users.query.get(userID)
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
        return render_template('edituser.html', thisUser = thisUser, userToEdit = userToEdit)
    else:
        testUser = Users.query.get(1) #TEST USER ID
        return render_template('edituser.html', thisUser = testUser, userToEdit = userToEdit)


#Update User POST Route
@app.route("/updateUser/<userID>", methods=["POST"])
def updateUser(userID):
    userToEdit = Users.query.get(userID)

    admin = request.form['admin']
    firstName = request.form['first_name']
    lastName = request.form['last_name']
    email = request.form['email']
    creator_name = request.form['creator_name']
    earnings_tips = request.form['earnings_tips']
    earnings_donations = request.form['earnings_donations']
    earnings_watcher_seconds = request.form['earnings_watcher_seconds']
    fb_user_id = request.form['fb_user_id'] # currently not working

    userToEdit.admin = admin == "True"
    userToEdit.first_name = firstName
    userToEdit.last_name = lastName
    userToEdit.email = email
    userToEdit.creator_name = creator_name
    userToEdit.earnings_tips = earnings_tips
    userToEdit.earnings_donations = earnings_donations
    userToEdit.earnings_watcher_seconds = earnings_watcher_seconds

    db.session.add(userToEdit)
    db.session.commit()


    return redirect("/admin")


#Delete User Route
@app.route("/deleteUser/<userID>")
def deleteUser(userID):
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])    #will need to check what it's actually called in session
    else:
        thisUser = Users.query.get(1) #TEST USER
    userToEdit = Users.query.get(userID)
    if thisUser.admin == True:   #make sure person trying to delete this User is an admin
        db.session.delete(userToEdit)
        db.session.commit()
        return redirect("/admin")
    else:
        return redirect("/")



























if __name__ == "__main__":
    app.run(debug=True)

