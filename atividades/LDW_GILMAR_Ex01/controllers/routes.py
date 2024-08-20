from flask import render_template, request, redirect, url_for

jogadores = []
personagens = [{'nome': 'Senshi', 'classe': 'Guerreiro', 'raca': 'Anão', 'tendencia': 'Neutro e Bom', 'antecedente': 'Sábio'}]

def init_app(app):
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/players', methods=['GET', 'POST'])
    def players():
        if request.method == 'POST':
            if request.form.get('jogadores'):
                jogadores.append(request.form.get('jogadores'))
            return redirect(url_for('players'))
                
        return render_template('jogadores.html', jogadores=jogadores, personagens=personagens)
    
    @app.route('/chips', methods=['GET', 'POST'])
    def chips():
        if request.method == 'POST':
            if request.form.get('nome') and request.form.get('classe') and request.form.get('raca') and request.form.get('tendencia') and request.form.get('antecedente'):
                personagens.append({'nome' : request.form.get('nome'), 'classe' : request.form.get('classe'), 'raca' : request.form.get('raca'), 'tendencia' : request.form.get('tendencia'), 'antecedente' : request.form.get('antecedente')})
            return redirect(url_for('chips'))
                
        return render_template('fichas.html', personagens=personagens)