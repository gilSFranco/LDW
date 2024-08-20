from flask import Flask, render_template
from datetime import date

# Instância do Flask, informando o parâmetro "__main__" e a pasta de views
app = Flask(__name__, template_folder='views')


@app.route("/")  # Decorator para o método app.route
def home():  # View function (função de visão)
    currentDate = date.today()
    # Renderizando a página HTML
    return render_template('index.html', currentDate=currentDate)


@app.route("/games")
def games():
    game = {
        'title': 'Pokemon Fire Red',
        'year': 2004,
        'category': 'Aventura'
    }
    currentYear = date.today().year
    players = ['Gilmar Soares', 'Lauany Mariano',
               'Victor Luís', 'Gustavo Kawamoto']
    return render_template('games.html',
                           game=game,
                           currentYear=currentYear,
                           players=players)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
