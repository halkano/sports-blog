import unittest
from app import db
from app.models import Blog,User


class BlogMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_halkano = User(username = 'halkano',password = '1234')
       self.new_blog = Blog(content='halkano')


   def test_check_instance_variable(self):
       self.assertEquals(self.new_blog.content,'halkano')
