# Vote Models from sql alchemy and data keys
from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey
# Vote class to upload votes on posts 
class Vote(Base):
  __tablename__ = 'votes'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post_id = Column(Integer, ForeignKey('posts.id'))