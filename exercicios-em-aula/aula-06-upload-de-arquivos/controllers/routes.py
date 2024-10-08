import urllib.request
from flask import render_template, request, redirect, url_for, flash, session
from markupsafe import Markup
from datetime import date
import urllib
import json
from models.database import db, Game, User, Imagem
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid


def init_app(app):
    players = []
    gamelist = [{
        'title': 'Pokemon Fire Red',
        'year': 2004,
        'category': 'Aventura'
    }]
    
    @app.before_request
    def check_auth():
        routes = ['login', 'caduser', 'home']

        if request.endpoint in routes or request.path.startswith('/static'):
            return

        if 'user_id' not in session:
            return redirect(url_for('login'))
    
    @app.route("/")
    def home():
        currentDate = date.today()
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
        
    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form['email']
            password = request.form['senha']
            user = User.query.filter_by(username=email).first()
            if user and check_password_hash(user.password, password):
                session['user_id'] = user.id
                session['email'] = user.username
                nickname = user.username.split('@')
                flash(
                    f'Login bem-sucedido! Bem-vindo {nickname[0].capitalize()}', 'success')
                return redirect(url_for('home'))
            else:
                flash("Falha no login! Verifique seu nome de usuário e senha.", 'danger')
        return render_template("login.html")

    @app.route("/caduser", methods=["GET", "POST"])
    def caduser():
        if request.method == "POST":
            email = request.form['email']
            password = request.form['senha']
            user = User.query.filter_by(username=email).first()
            if user:
                msg = Markup("Usuário já cadastrado. Faça <a hfre='/login'>login.</a>")
                flash(msg, 'danger')
                return redirect(url_for('caduser'))
            else:
                hashed_password = generate_password_hash(password, method="scrypt")
                new_user = User(username=email, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Registro realizado com sucesso! Faça o login!', 'success')
                return redirect(url_for("login"))
            
        return render_template("caduser.html")

    @app.route('/logout', methods=["GET", "POST"])
    def logout():
        session.clear()
        return redirect(url_for('home'))
    
    FILE_TYPES = set(['png', 'jpg', 'jpeg', 'gif', 'jfif', 'webp'])
    def arquivos_permitidos(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in FILE_TYPES
    
    @app.route('/galeria', methods=["GET", "POST"])
    def galeria():
        imagens = Imagem.query.all()
        
        if request.method == "POST":
            file = request.files['file']
            
            if not arquivos_permitidos(file.filename):
                flash("Utilize os tipos de arquivos referentes a imagem.", "danger")
                return redirect(request.url)
            
            filename = str(uuid.uuid4())
            
            img = Imagem(filename)
            db.session.add(img)
            db.session.commit()
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Imagem enviada com sucesso!", "success")
        
        return render_template('galeria.html', imagens=imagens)
    