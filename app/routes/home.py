from flask import Blueprint, render_template
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
  return render_template(
  'homepage.html',
  posts=posts
)
# login view route
@bp.route('/login')
def login():
  return render_template('login.html')
# post view route
@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
    'single-post.html',
    post=post
  )