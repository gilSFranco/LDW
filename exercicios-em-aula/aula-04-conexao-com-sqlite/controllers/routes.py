import urllib.request
from flask import render_template, request, redirect, url_for
from datetime import date
import urllib
import json
from models.database import db, Game

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
            return redirect(url_for('games'))

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
            return redirect(url_for('cadGames'))
        
        return render_template('cadGames.html',
                               gamelist=gamelist)
        
    @app.route("/apigames", methods=['GET', 'POST'])
    @app.route("/apigames/<int:id>", methods=['GET', 'POST'])
    def apiGames(id=None):
        
        url = 'https://www.freetogame.com/api/games'
        res = urllib.request.urlopen(url)
        data = res.read()
        gamesjson = json.loads(data)
        
        if id:
            ginfo = []
            
            for g in gamesjson:
                if g['id'] == id:
                    ginfo = g
                    break
                
            if ginfo:
                return render_template('gameinfo.html', ginfo=ginfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gamesjson=gamesjson)

    @app.route('/estoque', methods=['GET', 'POST'])
    @app.route('/estoque/delete/<int:id>', methods=['GET', 'POST'])
    def estoque(id=None):
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            
            return redirect(url_for('estoque'))
        
        if request.method == "POST":
            newgame = Game(
                request.form['titulo'], 
                request.form['ano'], 
                request.form['categoria'], 
                request.form['plataforma'], 
                request.form['preco'], 
                request.form['quantidade']
            )
            
            db.session.add(newgame)
            db.session.commit()
            
            return redirect(url_for('estoque'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 5
            
            games_page = Game.query.paginate(page=page, per_page=per_page)
            return render_template('estoque.html', gamesestoque=games_page)
        
    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    def edit(id):
            game = Game.query.get(id)
            
            if request.method == "POST":
                game.titulo = request.form['titulo']
                game.ano = request.form['ano']
                game.categoria = request.form['categoria']
                game.plataforma = request.form['plataforma']
                game.preco = request.form['preco']
                game.quantidade = request.form['quantidade']
                
                db.session.commit()
                
                return redirect(url_for('estoque'))
            
            return render_template('editgame.html', editgame=game)
        
