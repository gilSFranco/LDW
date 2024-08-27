from flask import Flask, render_template
from controllers import routes
from models.database import db
import os

os.system('cls')


# Instância do Flask, informando o parâmetro "__main__" e a pasta de views
app = Flask(__name__, template_folder='views')

routes.init_app(app)

dir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/games.sqlite3');

if __name__ == '__main__':
    db.init_app(app=app)
    # Criando um contexto de requisição fictícia
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=5000, debug=True)
