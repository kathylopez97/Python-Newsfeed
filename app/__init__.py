# import flask 
from flask import Flask
# import app routes dashboard and api
from app.routes import home, dashboard, api
# import app db to call app from all metadata
from app.db import init_db
# implement filters in template files
from app.utils import filters
from app.routes import home, dashboard, api
def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

   # implement filters in template files 
  app.jinja_env.filters['format_url'] = filters.format_url
  app.jinja_env.filters['format_date'] = filters.format_date
  app.jinja_env.filters['format_plural'] = filters.format_plural



  @app.route('/hello')
  def hello():
    return 'hello world'
  
  # register routes home, dashboard and api
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  app.register_blueprint(api)
  # Initialize database
  init_db(app)


  
  return app

