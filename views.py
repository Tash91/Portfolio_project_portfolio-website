from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route("/" , methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
       return redirect(url_for('about'))
         

    return render_template('home.html')


@app.route("/about-me" , methods=['GET', 'POST'])
def about():
    return render_template('about_me.html')

