class Post:
    def __init__(self, title, url, price):
        self._title = title
        self._url = url 
        self._price = price
    
    #TITLE SETTER, GETTER, DELETER
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @title.deleter
    def title(self):
        del self._title

    #URL SETTER, GETTER, DELETER
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @url.deleter
    def url(self):
        del self._url

    #PRICE SETTER, GETTER, DELETER
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
    
    @price.deleter
    def price(self):
        del self._price
