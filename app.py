from flask import Flask
from models import db
from routes.episodes import episodes_bp
from routes.guests import guests_bp
from routes.appearances import appearances_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(episodes_bp, url_prefix='/episodes')
app.register_blueprint(guests_bp, url_prefix='/guests')
app.register_blueprint(appearances_bp, url_prefix='/appearances')

if __name__ == '__main__':
    app.run(debug=True)
