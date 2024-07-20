# create a login and signup api
from flask import Blueprint, request, jsonify, session
from app.models import User
from app.db import get_db
import sys
bp = Blueprint('api', __name__, url_prefix='/api')
# return users to post and define signup form
@bp.route('/users', methods=['POST'])
def signup():
  data = request.get_json()
  db = get_db()
  

  try:
    # attempt creating a new user
    newUser = User(
      username = data['username'],
      email = data['email'],
      password = data['password']
    )

    db.add(newUser)
    db.commit()
  except:
      print(sys.exc_info()[0])
# session object to signup route
      session.clear()
      session['user_id'] = newUser.id 
      session['loggedIn'] = True

  # insert failed, so rollback and send error to front end
  db.rollback()
  return jsonify(message = 'Signup failed'), 500

  return jsonify(id = newUser.id)
# a new post route to be able to log out session
@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204
# post route 
@bp.route('/users/login', methods=['POST'])
def login():
  data = request.get_json()
  db = get_db()
# database is hashed  to verify email
  try:
   user = db.query(User).filter(User.email == data['email']).one()
  except:
   print(sys.exc_info()[0])
   # if function to verify password if false
   if user.verify_password(data['password']) == False:
    return jsonify(message = 'Incorrect credentials'), 400
 # created a session once logged and user id
  session.clear()
  session['user_id'] = user.id
  session['loggedIn'] = True

  return jsonify(id = user.id)