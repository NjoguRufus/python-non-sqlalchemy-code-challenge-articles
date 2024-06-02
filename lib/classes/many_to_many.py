class Article:
    all = []

    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)


    def title(self):
        return self._title

    def title(self, new_title):
        if self._title is not None:
            raise AttributeError("Title cannot be changed")
        if isinstance(new_title, str):
            if 5 <= len(new_title) <= 50:
                self._title = new_title
            else:
                raise ValueError("Title must be between 5 and 50 characters")
        else:
            raise TypeError("Title must be a string")

    def author(self):
        return self._author

    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise TypeError("Author must be an instance of Author")
        self._author = new_author

    def magazine(self):
        return self._magazine

    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        self._magazine = new_magazine

    def __repr__(self):
        return f'<Article: author={self.author.name}, magazine={self.magazine.name}, title="{self.title}">'

class Author:
    def __init__(self, name):
        self._name = None
        self.name = name

    def name(self):
        return self._name

    def name(self, new_name):
        if self._name is not None:
            raise AttributeError("Name cannot be changed")
        if isinstance(new_name, str):
            if len(new_name) > 0:
                self._name = new_name
            else:
                raise ValueError("Name must be longer than 0 characters")
        else:
            raise TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        return topic_areas if topic_areas else None

    def __repr__(self):
        return f'<Author: name={self.name}>'

class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category

    def name(self):
        return self._name

    def name(self, new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else:
                raise ValueError("Name must be between 2 and 16 characters")
        else:
            raise TypeError("Name must be a string")

    def category(self):
        return self._category

    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category) > 0:
                self._category = new_category
            else:
                raise ValueError("Category must be longer than 0 characters")
        else:
            raise TypeError("Category must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [article.title for article in self.articles()]
        return article_titles if article_titles else None

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1
        list_of_authors = [author for author, count in authors.items() if count >= 2]
        return list_of_authors if list_of_authors else None

    def __repr__(self):
        return f'<Magazine: name={self.name}, category={self.category}>'
