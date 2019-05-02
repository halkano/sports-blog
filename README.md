 # [Sports-blog]
Built By Henry halkano

## Description

Sports-blog is a website where you can create and share your opinions and other users can read and comment on them.
You can view the site at:Heroku

## User Stories These are the behaviours/features that the application implements for use by a user.


| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Signup | string text | Creates user account |
| Login | string text | logs in to user account |
| Submit new pitch | string text | new pitch from user |
| down vote a pitch | Click on the downvote button | adds +1 downvote  |
| up vote a pitch | Click on the upvote button |adds +1 upvote |
| Add comment to pitch | String text  | New comment to pitch selected |
| View posted pitch | Click on pitch categories  | Display pitches in that category |
| View user pitch | Click on user profile  | Display pitches posted by the user|




$ git clone https://github.com/Halkano/sports-BLog/
$ cd sports-blog
 Running the Application
Creating the virtual environment

$ python3.6 -m venv --without-pip virtual $
source virtual/bin/env
$ curl https://bootstrap.pypa.io/get-pip.py |

## Set-up and Installation

-$ python3.6 -m pip install Flask
 -$ python3.6 -m pip install Flask-Bootstrap
-$ python3.6 -m pip install Flask-Script

#### Insert the following info into it:
-python3.6 manage.py server

#### To run the application, in your terminal:
-$ chmod +x start.sh $
-./start.sh

#### Testing the Application To run the tests for the class files:
-$ python3.6 manage.py tests

###### Technologies Used
-Python3.6 Flask

-License Copyright (c) 2018  Henry Halkano
 
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
