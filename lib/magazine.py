from article import Article  

class Magazine:
    all_magazines = []  

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)  # Add the magazine instance to all_magazines list

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        authors = [article.author for article in self._articles]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [article.author for article in self._articles]
        unique_authors = set(authors)
        return [author for author in unique_authors if authors.count(author) > 2]

    def add_article(self, author, title):
        article = Article(author, self, title)  # Create Article instance
        self._articles.append(article)  # Add the article to the magazine's articles list
        return article

    @classmethod
    def top_publisher(cls):
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))