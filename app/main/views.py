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
   blogs = Blog.query.all()
   title = 'Sports-blogs'
   return render_template('index.html',quote = quote,quote_author = quote_author,title=title,blogs=blogs)
