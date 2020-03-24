
from sqlalchemy.sql import func
from config import db
from sqlalchemy import text
from flask_migrate import Migrate



# - Users Table:
#     - OAuth UserID

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    creator_name = db.Column(db.String(255))
    user_avatar = db.Column(db.String(255))     #allow user to upload 32x32 avatar, must be sanitized on upload
    # oauth_link = db.Column(db.String(255))    #link to OAuth UserID
    earnings_tips = db.Column(db.Float)
    earnings_donations = db.Column(db.Float)
    description = db.Column(db.Text)
    user_image = db.Column(db.String(255))  #retrieve from OAuth Facebook Picture, default will be path to default avatar
    stream = db.relationship("Streams", uselist = False, backref = "creator")
    videos = db.relationship("Videos", backref = "creator")
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return "UserID: " + self.id + " Name: " + self.first_name + " " + self.last_name

class Videos(db.Model):
    __tablename__ = "Videos"
    id = db.Column(db.Integer, primary_key = True)
    video_link = db.Column(db.String(255)) #url of video from whatever platform used
    num_times_watched = db.Column(db.Integer, default = 0)
    earnings_tips = db.Column(db.Float)
    earnings_donations = db.Column(db.Float)
    description = db.Column(db.Text)
    video_author_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


    def __repr__(self):
        return "VideoID: " + self.id + " video_author_id: " + self.video_author_id

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
    stream_author_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __repr__(self):
        return "StreamID: " + self.id + " stream_author_id: " + self.stream_author_id


































