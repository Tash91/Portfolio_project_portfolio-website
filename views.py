from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hhome():
    return render_template('base.html')