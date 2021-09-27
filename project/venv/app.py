from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('show+nswers.html')
 
app.run(host='localhost', port=5000)