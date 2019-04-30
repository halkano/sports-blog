from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quotes

# Views
@main.route('/')
def index():
   '''
   This is the home page view.
   '''
   myquote = get_quotes()
   quote = myquote['quote']
   quote_author = myquote['author']
   title = 'Home - Welcome to The best quotes Review Website Online'
   return render_template('index.html',quote = quote,quote_author = quote_author,title=title)
