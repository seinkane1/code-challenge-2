class Article:
    _all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article._all_articles.append(self)


    def all(cls):
        return cls._all_articles