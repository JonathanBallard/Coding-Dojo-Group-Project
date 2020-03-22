# Project - Speakeasy
## MVP Features
- User - Login/Registration with OAuth (Facebook API) - RESEARCH IN PROGRESS
- Creator - Login/Registration (possibly use their Facebook page to host videos) _<--Every User will be a creator_
- Create CRUD operations for both creator accounts and customer accounts _<--No need, if using OAuth I doubt we'll be able to edit their user info_
- Ability to see recorded video alongside chat (live video will be a stretch goal) _<-- I thought we were making the video part a backlog feature?_
- Most likely will utilize Facebook, IG, Youtube, or Twitch API to display stream.
- Accept "code" or "keyword" that allows members to join the channel/video/gain access _<-- How are people going to be given/sold these codes?_
## Feature Backlog
- Have multiple codes and livestreams _<--building one stream per user currently, what do you mean by multiple codes/livestreams?_
- Create a refillable "bank" of credits for users to use up while watching videos and determine the timeuse with an algorithm. (each second is $0.001 so each minute is $0.06) - This is the business model.

## TODO: MVP

- Database First!!! Must contain: Users table, Videos table, Streams table
- Login/Registration with either with OAuth or with our own system
- Account Administration Page to edit users __(only if using our own login/registration system)__
- Each user has /videos page where all recordings are
- Each user has /stream page where streams would go in the future
- Each user has /user page where they enter a description of themselves and maybe a picture, from here they access the /portal to videos/stream
- /portal page which requires the creator code/password in order to enter videos or stream
- Each user has a /stats page where they can see how much money they've earned through time and through tips
- Each /stream page has a chat room

## TODO: Backlog

- Add one of the media platforms for recorded/streaming video
- /create page with video and info
- /display after logging in you can see which channels are live/which channels have videos uploaded (once that feature is complete)

### Proposed Features & Assignment: MVP

- Feature (estimated length of time to complete) __Assigned Person__
- Database (Med/Long) __Jonathan__
- Wireframe the Pages (login/registration, portal, videos, stream, stats) (Med/Short) __Tanner__
- Login/Registration Page with OAuth (Med) __Tanner__
- User Page & Route (/user page) (Short) where users can put a description of themselves and a picture __Jonathan__
- User Page & Route (/portal page) (Short) where users enter their "code" in to view a stream/video __Sol__
- User Page & Route (/videos page) (Short) show total views, with static videos for the moment __Tanner__
- User Page & Route (/stream page) (Short) show current viewer number, with a static video for the moment __Tanner__
- User Page & Route (/stats page) (Short) where users can create their "code", view their earnings __Jonathan__
- Chat Function for user /stream Pages (Long) __Sol__
- Page Design/Colors/Beautify (Med) __Jonathan__

### Features: Backlog

- /display page (off of home page, displays all currently active creator pages for people to scroll through with most active at top)
- Video Functions for user /videos Pages
- Streaming Functions for user /stream Pages
- /create page where User puts their video, title, description, keycode, etc..


























