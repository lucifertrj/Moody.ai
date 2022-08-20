from flask import Flask,session,render_template,flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def home_page():
    return render_template("index.html")
    
if __name__ == '__main__':
    app.run(debug=False)
    