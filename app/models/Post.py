from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, select, func
from sqlalchemy.orm import relationship, column_property
# post class models to create table data 

class Post(Base):
  __tablename__ = 'posts'
  id = Column(Integer, primary_key=True)
  title = Column(String(100), nullable=False)
  post_url = Column(String(100), nullable=False)
  user_id = Column(Integer, ForeignKey('users.id'))
  created_at = Column(DateTime, default=datetime.now)
  updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
 #  enable user data information
  user = relationship('User')
  # enable comments to be posted or deleted
  comments = relationship('Comment', cascade='all,delete')
   # enables votes to be deleted
  votes = relationship('Vote', cascade='all,delete')


  
  