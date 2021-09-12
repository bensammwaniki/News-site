from flask import Flask,render_template
from .import main
from ..request import get_sources,get_articles

@main.route('/')

def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')