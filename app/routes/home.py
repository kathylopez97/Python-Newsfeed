from flask import Blueprint, render_template, session, redirect
# import post models and get databases
from app.models import Post
from app.db import get_db
bp = Blueprint('home', __name__, url_prefix='/')
# homepage view route
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = (
  db
    .query(Post)
    .order_by(Post.created_at.desc())
    .all()
)
  # update return statement to pass login session to the template
  # created a session in homepage html
  return render_template(
  'homepage.html',
  posts=posts,
  loggedIn=session.get('loggedIn')
)
# login view route
@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')
# post view route
@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template to single route session
  return render_template(
  'single-post.html',
  post=post,
  loggedIn=session.get('loggedIn')
)