from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os


template_dir = os.path.abspath('./frontend/')

app = Flask(__name__, template_folder=template_dir)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("ta funfando alguma coisa")
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'failed'})   
    if request.method == 'GET':
        return render_template('index.html')


app.run(debug=True, port=8000)
