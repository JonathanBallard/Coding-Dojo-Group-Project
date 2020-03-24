
from sqlalchemy.sql import func
from config import db
from sqlalchemy import text
from flask_migrate import Migrate



# - Users Table:
#     - some link to the OAuth user (likely their facebook email)
#     - a one-to-many relationship between Users and Video with a backref
#     - a one-to-one relationship between Users and Stream with backref
# - Video Table:
#     - the foreign key from Users
#     - video length (so we can list it on /display page), perhaps we can get this from the video when we receive it, must study embedding
# - Stream Table:
#     - the foreign key from Users

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    creator_name = db.Column(db.String(255))
    user_avatar = db.Column(db.String(255))     #allow user to upload 32x32 avatar, must be sanitized on upload
    # oauth_link = db.Column(db.String(255))    #link to OAuth
    earnings_tips = db.Column(db.Float)
    earnings_donations = db.Column(db.Float)
    description = db.Column(db.Text)
    user_image = db.Column(db.String(255))  #will be relative path to image, all images must be sanitized upon upload, being named an incremental number, perhaps pictures will be a database column and we can use ID instead
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class Videos(db.Model):
    __tablename__ = "Videos"
    id = db.Column(db.Integer, primary_key = True)
    video_link = db.Column(db.String(255)) #url of video from whatever platform used
    num_times_watched = db.Column(db.Integer, default = 0)
    earnings_tips = db.Column(db.Float)
    earnings_donations = db.Column(db.Float)
    description = db.Column(db.Text)
    video_password = db.Column(db.String(255)) #creator code, must be input by users in order to enter
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class Streams(db.Model):
    __tablename__ = "Streams"
    id = db.Column(db.Integer, primary_key = True)
    stream_link = db.Column(db.String(255)) #the link to the stream from whatever platform we use
    num_current_watchers = db.Column(db.Integer, default = 0)
    earnings_tips = db.Column(db.Float)
    earnings_donations = db.Column(db.Float)
    earnings_watcher_seconds = db.Column(db.Float) #how much money earned from the seconds of all watchers combined
    amount_watcher_seconds = db.Column(db.Time) #number of seconds that all watchers combined have spent on this stream
    description = db.Column(db.Text)
    time_running = db.Column(db.Time)
    stream_password = db.Column(db.String(255)) #creator code, must be input by users in order to enter
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)




































