# Python3
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Pull html file to run
@app.route('/calculator')
def index():
    return render_template('calculator.html')

# App running on X host
if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)