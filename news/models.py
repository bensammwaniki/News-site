class Articles:
    
    '''
    Articles class 
    '''
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name 
        self.author = author
        self.title = title
        self.description = description
        self.url = url 
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Sources:
    '''
    Class to define news sources
    '''
    
    def __init__(self,id,name,description,url,category,language):
        self.id = id
        self.name = name 
        self.description = description
        self.url = url 
        self.category = category
        self.language = language

class Everything:
        ''''
        class that create all the articles
        '''
        def __init__(self,author,title,description,url,urlToImage,publisherAt,content):
            self.author=author
            self.title=title
            self.description=description
            self.url=url
            self.urlToImage=urlToImage
            self.publisherAt=publisherAt
            self.content=content        