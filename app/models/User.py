from app.db import Base
from sqlalchemy import Column, Integer, String
# this function validates 
from sqlalchemy.orm import validates
# import bcrpyt to secure password
import bcrypt
salt = bcrypt.gensalt()
# this function creates user table 
class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)

# protects the data using email
  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email
    return email
  
  # validate function to assert password greater than 4 characters

  @validates('password')
  def validate_password(self, key, password):
   assert len(password) > 4
  
   # encrypt password
   return bcrypt.hashpw(password.encode('utf-8'), salt)
   # verify password from email
  def verify_password(self, password):
   return bcrypt.checkpw(
    password.encode('utf-8'),
    self.password.encode('utf-8')
  )