import urllib.request,json
from .models import Articles,Sources


sources_url = None
articles_url = None

def configure_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['API_KEY']
    sources_url = app.config['SOURCES_URL']
    articles_url = app.config['ARTICLES_URL']