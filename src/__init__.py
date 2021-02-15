from .app import create_app

# load modules
from src.blueprints.blueprint_x import blueprint_x
from src.blueprints.blueprint_y import blueprint_y

# from flask_migrate import Migrate
# from models import User as UserModel, db
# from flask_restful import Api
# from resources import HealthCheck, UserList, User

app = create_app()

# register blueprints. ensure that all paths are versioned!
app.register_blueprint(blueprint_x, url_prefix="/api/v1/blueprint_x")
app.register_blueprint(blueprint_y, url_prefix="/api/v1/blueprint_y")
