from flask import render_template, request
from datetime import date

players = []
gamelist = [{
    'title': 'Pokemon Fire Red',
    'year': 2004,
    'category': 'Aventura'
}]


def init_app(app):
    @app.route("/")  # Decorator para o método app.route
    def home():  # View function (função de visão)
        currentDate = date.today()
        # Renderizando a página HTML
        return render_template('index.html', currentDate=currentDate)

    @app.route("/games", methods=['GET', 'POST'])
    def games():
        currentYear = date.today().year
        game = gamelist[0]

        if request.method == 'POST':
            if request.form.get('player'):
                players.append(request.form.get('player'))

        return render_template('games.html',
                               game=game,
                               currentYear=currentYear,
                               players=players)

    @app.route("/cadgames", methods=['GET', 'POST'])
    def cadGames():
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({
                    'title': request.form.get('title'),
                    'year': request.form.get('year'),
                    'category': request.form.get('category')
                })
        return render_template('cadGames.html',
                               gamelist=gamelist)
