from flask import Flask, render_template

app = Flask("Hello")

@app.route('/')
@app.route("/hello")

@app.route("/tchau")

def hello():
    return render_template("hello.html")

