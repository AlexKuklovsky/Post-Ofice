from flask import Flask, render_template, request
import os
import json
    
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit_package():
    return "Form submitted!"

if __name__ == '__main__':
    app.run(debug=True)
