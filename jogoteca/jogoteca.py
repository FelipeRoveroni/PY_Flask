from flask import Flask, render_template, request

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

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    Jogo = jogo(nome, categoria, console)
    lista.append(Jogo)
    return render_template('lista.html', titulo='jogos', jogos=lista)
    
app.run(debug=True)
