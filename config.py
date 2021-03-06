import os

class Config:
    '''
    General configurations
    '''
    
    SOURCES_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-09-12&sortBy=popularity&apiKey={}'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_API_KEY = os.environ.get('API_KEY')  

class ProdConfig(Config):
    '''
    Production  configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}  