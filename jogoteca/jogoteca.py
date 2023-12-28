from flask import Flask, render_template

class jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1= jogo('Tetris', 'Puzzle', 'Atari')
    jogo2= jogo('CS:GO', 'FPS', 'PC')
    jogo3= jogo('Minecraft', 'Sobrevivencia', 'MultiPlataforma')
    
    
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run()
