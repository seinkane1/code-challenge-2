class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

        Magazine._all_magazines.append(self)

   
    def name(self):
        
        return self._name

  
    def category(self):
        return self._category

    def articles(self):
        
        return self._articles

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(set(authors))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors_dict = {}
        for article in self.articles():
            
            author = article.author
            
            if author in authors_dict:
                authors_dict[author] += 1
            else:
                
                authors_dict[author] = 1

        return [author for author, count in authors_dict.items() if count > 2]

    
    def top_publisher(cls):
        if not cls._all_magazines:
            return None

        most_articles_magazine = max(cls._all_magazines, key=lambda x: len(x.articles()))
        return most_articles_magazine