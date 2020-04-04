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
@app.route("/register", methods=["POST", "GET"])
def registration():
    # if request.method == 'POST':
    #     print(request.get_json())
    #     fbData = request.get_json()
    new_user = Users.add_new_user(request.form)
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    session['user_id'] = new_user.id
    return redirect("/user")

# @app.route("/handle_json", methods=["POST"])
# def handler():
#     data = request.get_json()
#     print(data)
#     return redirect('/user')

#User Profile Page
@app.route("/user/<userID>")
def user(userID):
    if 'user_id' in session:
        thisUser = Users.query.get(session['user_id']) 
        return render_template("user.html", thisUser = thisUser)
    else:
        return redirect('/')

#Stream Page
# BLAH







#Stats Page
@app.route("/stats")
def statsRoute():
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


#Create Video
@app.route("/createVideo/<userID>", methods=['POST'])
def createVideo(userID):
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])
        newVid = Videos(title = request.form['title'], video_link = request.form['video_link'], description = request.form['description'], video_author_id = session['user_id'])
        db.session.add(newVid)
        db.session.commit()
        return redirect('/create')
    else:
        return redirect('/create')


#Admin Page
@app.route("/admin")
def adminPage():
    testUser = Users(first_name = "NOT", last_name = "A", email = "USER", admin = False, creator_name = "testcase", description = "description")
    db.session.add(testUser)
    db.session.commit()
    allUsers = Users.query.all()
    
    # Check if User is Admin, if so allow them access
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])
        if thisUser.admin == True:
            return render_template('admin.html', thisUser = thisUser, allUsers = allUsers)
        else:
            return redirect('/')
    else:
        testUser = Users.query.get(1) #TEST USER ID
        return render_template('admin.html', thisUser = testUser, allUsers = allUsers)


#Edit User Page
@app.route("/editUser/<userID>")
def editUserPage(userID):
    userToEdit = Users.query.get(userID)
    # Check if User is Admin, if so allow them access
    if "user_id" in session:
        thisUser = Users.query.get(session['user_id'])
        if thisUser.admin == True:
            return render_template('edituser.html', thisUser = thisUser, userToEdit = userToEdit)
        else:
            return redirect('/')
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
    fb_user_id = request.form['fb_user_id'] # currently not working, do not use

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
    app.run(debug=True, ssl_context='adhoc')
