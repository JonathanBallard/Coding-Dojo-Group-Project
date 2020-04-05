# Project - Speakeasy

## MVP Features

- User - Login/Registration with OAuth (Facebook API) - RESEARCH IN PROGRESS
- Create CRUD operations for user accounts
- Ability to see recorded video alongside chat
- Most likely will utilize Facebook, IG, Youtube, or Twitch API to display stream.

## Feature Backlog

- Streaming Video
- Create a refillable "bank" of credits for users to use up while watching videos and determine the timeuse with an algorithm. (each second is $0.001 so each minute is $0.06) - This is the business model.

## TODO: MVP

- Database First!!! Must contain: Users table, Videos table, Streams table
- Login/Registration with either with OAuth or with our own system
- Account Administration Page to edit users __(only if using our own login/registration system)__
- Each user has /videos page where all recordings are
- Each user has /stream page where streams would go in the future
- Each user has /user page where they enter a description of themselves and maybe a picture, from here they access to the videos/stream
- Each user has a /stats page where they can see how much money they've earned through time and through tips
- Each /stream page has a chat room

## TODO: Backlog

- Add one of the media platforms for recorded/streaming video
- /create page with video and info
- /display after logging in you can see which channels are live/which channels have videos uploaded (once that feature is complete)

## Proposed Features & Assignment: MVP

- Feature (estimated length of time to complete) __Assigned Person__

#### Primary Functionality (AKA First Priority)

- Database (Med/Long) __Jonathan__ **DONE**
- Chat Function for user /stream Pages (Long) __Sol__ **TEST**
- Login/Registration Page including OAuth (Med) __Tanner__

#### Remaining Requirements for MVP

- Wireframe the Pages (login/registration, portal, videos, stream, stats) (Med/Short) __Tanner__ **DONE**
- User Page & Route (/user page) (Short) where users can put a description of themselves and a picture __Sol__
- User Page & Route (/stream page) (Short) show current viewer number, with a static video for the moment __Sol__
- User Page & Route (/stats page) (Med/Short) list of all user's videos where user can view their earnings per video, total earnings, earnings from stream __Jonathan__ **DONE**
- Account Administration, list of user accounts /admin page (Med/Short) __Jonathan__ **DONE**
- Account Administration, CRUD to edit User Accounts /editUser page (Med/Short) __Jonathan__ **DONE**
- Links connecting the pages where they need to be connected, User Page to Stream, to Create, to Stats __Tanner__

#### These Features Only Added After Everything Else Done

- Video Functions for user /videos Pages, should just be embedding (Short) __Tanner__ **SKIPPED**
- /create page where User puts their video, title, description, etc.. (Med) __Jonathan__ **DONE**
- Page Design/Colors/Beautify (Med) __Jonathan__
- User Page & Route (/videos page) (Med/Short) show total views, with static videos for the moment __Tanner__ **SKIPPED**
- Login/Register takes you to your own User page __Sol__ **DONE**
- Make sure only Admin accounts access admin page/edituser page __Jonathan__ **DONE**

#### Lastly - Testing

- Test Login/Registration, ensure flask messages popup when login/registration fails
- Test /user page
- Test /videos page
- Test /stream page
- Test /stats page
- Test /admin page
- Test /editUser page
- Test /create page
- Test chat functions
- Test OAuth functions
- Test Database

## Features: Backlog

- /display page (off of home page, displays all currently active creator pages for people to scroll through with most active at top)
- Streaming Functions for user /stream Pages
- Mobile Friendly
