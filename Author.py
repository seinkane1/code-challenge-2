class Author:
    def __init__(self, name):
        self._name = name

  
    def name(self):
        return self._name

    def articles(self):
        
        return [article for article in Article.all() if article.author == self]

    def magazines(self):
        
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        
        magazines = self.magazines()
        if not magazines:
            return None
        
        return list(set([magazine.category for magazine in magazines]))

    