import os
from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    
    return render_template('finHome.html')

@app.route('/login', methods = ['GET','POST'])
def login():

    
    
    return render_template('finLogin.html')


    

if __name__ == '__main__':
    app.run(debug=False)