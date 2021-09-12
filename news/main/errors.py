from flask import render_template
from . import main

@main.news_errorhandler(404)
def four_O_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404