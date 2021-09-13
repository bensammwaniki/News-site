
from flask import render_template
from .import main
from ..request import get_sources,get_articles,search_news


@main.route('/')
def index():
    title = 'This is the best News Center'
    news_sources = get_sources('general')
    articles = get_articles(id)

    return render_template('index.html',title = title,sources =news_sources,articles=articles)
# @main.route('/articles/<id>')

# def articles(id):    
#     return render_template('articles.html',id = id, articles=articles)    

def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search {news_name}'
    return render_template('disp_search.html',news = searched_news,title=title)