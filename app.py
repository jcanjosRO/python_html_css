from flask import Flask, render_template, g
import sqlite3

DATABASE = "banco.bd"

SECRET_KEY = "chave"


app = Flask("Hello")

app.config.from_object(__name__)

def conecta_bd():
    return sqlite3.connect(DATABASE)

@app.before_request
def antes_requisicao():
    g.bd = conecta_bd()

@app.teardown_request
def depois_requisicao(e):
    g.bd.close()

@app.route("/")
def exibir_entradas():
    nome = "Jean"
    return render_template("hello.html")

