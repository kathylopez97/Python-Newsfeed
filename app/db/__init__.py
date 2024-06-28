from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()
# connect to database using env variable
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)
# close db connection
  app.teardown_appcontext(close_db)
# saves the current on the g object instrad of creating a new session every time
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()
  return g.db
# closes connection  to database to avoid opening number of sessions at the same time
def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()