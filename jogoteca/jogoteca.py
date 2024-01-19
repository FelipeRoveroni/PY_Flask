from flask import Flask, render_template, request, redirect, session, flash, url_for

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console
        
jogo1= jogo('Tetris', 'Puzzle', 'Atari')
jogo2= jogo('CS:GO', 'FPS', 'PC')
jogo3= jogo('Minecraft', 'Sobrevivencia', 'MultiPlataforma')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'Teste'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    Jogo = jogo(nome, categoria, console)
    lista.append(Jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + 'Logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Usuario não logado')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('LogOut efetuado com sucesso!')
    return redirect(url_for('index'))
    
app.run(debug=True)
