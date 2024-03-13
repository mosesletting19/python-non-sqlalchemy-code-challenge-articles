class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Invalid name for author")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception("Invalid name for magazine")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Invalid category for magazine")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            author = article.author
            if author in authors_count:
                authors_count[author] += 1
            else:
                authors_count[author] = 1
        return [author for author, count in authors_count.items() if count > 2]

    def add_article(self, author, title):
        article = Article(author, self, title)
        self._articles.append(article)
        return article

    @classmethod
    def top_publisher(cls):
        max_articles = 0
        top_magazine = None
        for magazine in cls.all_magazines:
            if len(magazine.articles()) > max_articles:
                max_articles = len(magazine.articles())
                top_magazine = magazine
        return top_magazine


class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Invalid author for article")
        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine for article")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Invalid title for article")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
