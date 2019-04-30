import unittest
from app import db
from app.models import Comment,User


class CommentMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_halkano = User(username = 'halkano',password = '1234')
       self.new_comment = Comment(content='halkano')


   def test_check_instance_variable(self):
       self.assertEquals(self.new_comment.content,'halkano')
