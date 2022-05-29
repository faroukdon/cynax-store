from flask import Flask
from flask_migrate import Migrate
from models.Product import db
from routes.product_bp import product_bp


app = Flask(__name__)

app.config.from_object('config')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(product_bp, url_prefix='/products')

@app.route('/')
def index():

    return ("hello Cynax Team im your testing  endpoint")




if __name__ == '__main__':

    app.debug = True

    app.run()
