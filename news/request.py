import urllib.request,json
from .models import Articles,Sources,Everything


sources_url = None
articles_url = None

def config_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['API_KEY']
    sources_url = app.config['SOURCES_URL']
    articles_url = app.config['ARTICLES_URL']

def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    sources_url = 'https://newsapi.org/v2/top-headlines/sources?apiKey=5885f46e6c344dc5bfdcce62211112b5'.format(sources)
    with urllib.request.urlopen(sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        
        sources_results = None
        
        if sources_response['sources']:
            sources_list = sources_response['sources']
            
            sources_results = process_sources(sources_list)
            
        return sources_results    

def process_sources(sources_list):
    '''
    Function that processesses the source results and turns them to a list of objects
    '''
    
    sources_results = []
    
    for source in sources_list:
        id = source.get('id')
        name = source.get("name")
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        
        if language == 'en':
            
            source_object =Sources(id,name,description,url,category,language)
            sources_results.append(source_object)
            
    return sources_results


def get_articles(articles):
    '''
    function to get json response
    '''
    
    articles_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=5885f46e6c344dc5bfdcce62211112b5'.format(articles)
    
    with urllib.request.urlopen(articles_url) as url:
        
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        
        articles_results = None
        
        if articles_response['articles']:
            articles_list =  articles_response['articles']
            articles_results = process_articles(articles_list)
            
        return articles_results
    
def process_articles(articles_list):
    
    articles_results = []
    
    for article in articles_list:
        id = article['source']['id']
        name = article.get('name')
        author = article.get('author')
        content = article.get('content')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        
        if urlToImage:
            articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
            
            articles_results.append(articles_object)
            
    return articles_results  

    # ============================================================================================================== 

def search_news(sources):
    search_news_headlines= 'https://newsapi.org/v2/everything?q={}&apiKey=5885f46e6c344dc5bfdcce62211112b5'.format(sources)
    with urllib.request.urlopen(search_news_headlines) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        if search_news_response['articles']:
            search_list = search_news_response['articles']
            search_results = process_everything(search_list)


    return search_results

def process_everything(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    '''
    news_sources_everything= []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        publisherAt=news_item.get('publisherAt')
        content=news_item.get('content')
        if description:
            news_object = Everything(author,title,description,url,urlToImage,publisherAt,content)
            news_sources_everything.append(news_object)

    return news_sources_everything         
def get_everything():
    '''
    function to retrieve data from database of newsapi
    '''  

    get_news_articles_url = 'https://newsapi.org/v2/everything?q=sports&apiKey=5885f46e6c344dc5bfdcce62211112b5'

    with urllib.request.urlopen(get_news_articles_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources_everything = None

        if get_news_response['articles']:
            news_sources_list = get_news_response['articles']
            news_sources_everything = process_everything(news_sources_list)


    return news_sources_everything

def process_everything(news_list):
    news_sources_everything= []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage=news_item.get('urlToImage')
        publisherAt=news_item.get('publisherAt')
        content=news_item.get('content')
        if description:
            news_object = Everything(author,title,description,url,urlToImage,publisherAt,content)
            news_sources_everything.append(news_object)    