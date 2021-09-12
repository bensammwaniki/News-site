from re import DEBUG
from flask import Flask, app,render_template
from flask_bootstrap import Bootstrap

App = Flask(__name__)
Bootstrap(App)

if __name__=="__main__":
    app.run(DEBUG=True)