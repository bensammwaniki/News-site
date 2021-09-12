
from flask import render_template
from .import main
from ..request import get_sources,get_articles


@main.route('/')
def index():
    title = 'Welcome to NewsWeb App'
    news_sources = get_sources('general')
    print(news_sources)
   
    
    return render_template('index.html',title = title,sources =news_sources)
@main.route('/articles/<id>')

def articles(id):    
    articles = get_articles(id)
    return render_template('articles.html',id = id, articles=articles)    