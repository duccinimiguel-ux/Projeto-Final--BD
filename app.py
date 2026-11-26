from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # substitua pela senha do seu MySQL
        database="bd_cadastro"
    )

from flask import request

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    # Captura os dados enviados
    nome = request.form["nome"]
    idade = request.form["idade"]
    cidade = request.form["cidade"]
    
    # Conecta ao banco e insere os dados
    conexao = conectar_db()
    cursor = conexao.cursor()
    
    comando = "INSERT INTO tb_cadastro (nome, idade, cidade) VALUES (%s, %s, %s)"
    valores = (nome, idade, cidade)
    
    cursor.execute(comando, valores)
    conexao.commit() # Salva as alterações no banco de dados
    
    cursor.close()
    conexao.close()
    
    return "Cadastro realizado com sucesso!"
