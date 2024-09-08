from flask import render_template, request, redirect, url_for
from models.database import db, Ficha, Jogador

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/players', methods=['GET', 'POST'])
    @app.route('/players/delete/<int:id>', methods=['GET', 'POST'])
    def players(id=None):
        if id:
            jogador = Jogador.query.get(id)
            db.session.delete(jogador)
            db.session.commit()
        
        if request.method == 'POST':
            novoJogador = Jogador(
                request.form['nome'],
                request.form['idade']
            )
            
            db.session.add(novoJogador)
            db.session.commit()
            
            return redirect(url_for('players'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 5
            
            jogadores_page = Jogador.query.paginate(page=page, per_page=per_page)
            return render_template('jogadores.html', jogadoresdamesa=jogadores_page)
        
    @app.route('/editplayer/<int:id>', methods=['GET', 'POST'])
    def editPlayer(id):
        jogador = Jogador.query.get(id)
        
        if request.method == "POST":
            jogador.nome = request.form['nome']
            jogador.idade = request.form['idade']
            
            db.session.commit()
            
            return redirect(url_for('players'))
        
        return render_template('editJogador.html', editjogador=jogador)
                
    
    @app.route('/chips', methods=['GET', 'POST'])
    @app.route('/chips/delete/<int:id>', methods=['GET', 'POST'])
    def chips(id=None):
        if id:
            ficha = Ficha.query.get(id)
            db.session.delete(ficha)
            db.session.commit()
        
        if request.method == 'POST':
            novaFicha = Ficha(
                request.form['nome'],
                request.form['classe'],
                request.form['antecedente'],
                request.form['raca'],
                request.form['tendencia'],
                request.form['forca'],
                request.form['destreza'],
                request.form['constituicao'],
                request.form['inteligencia'],
                request.form['sabedoria'],
                request.form['carisma']
            )
            
            db.session.add(novaFicha)
            db.session.commit()
            
            return redirect(url_for('chips'))
        else:
            page = request.args.get('page', 1, type=int)
            per_page = 5
            
            fichas_page = Ficha.query.paginate(page=page, per_page=per_page) 
            return render_template('fichas.html', personagensdamesa=fichas_page)
        
    @app.route('/editchip/<int:id>', methods=['GET', 'POST'])
    def editChip(id):
        ficha = Ficha.query.get(id)
        
        if request.method == 'POST':
            ficha.nome = request.form['nome']
            ficha.classe = request.form['classe']
            ficha.antecedente = request.form['antecedente']
            ficha.raca = request.form['raca']
            ficha.tendencia = request.form['tendencia']
            ficha.forca = request.form['forca']
            ficha.destreza = request.form['destreza']
            ficha.constituicao = request.form['constituicao']
            ficha.inteligencia = request.form['inteligencia']
            ficha.sabedoria = request.form['sabedoria']
            ficha.carisma = request.form['carisma']
            
            db.session.commit()
            
            return redirect(url_for('chips'))
        
        return render_template('editFicha.html', editficha=ficha)
            
    @app.route('/chips/<int:id>', methods=['GET', 'POST'])
    def findChipById(id):
        ficha = Ficha.query.get(id)
        return render_template('fichacompleta.html', fichacompleta=ficha)