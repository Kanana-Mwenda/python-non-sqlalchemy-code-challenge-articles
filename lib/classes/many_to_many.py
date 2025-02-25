class Article:
    all = [] #store all article instances

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        #store all article instances
        Article.all.append(self)

        #establish relationship
        self.magazine._authors.append(self.author) #store the authors
        self.magazine._articles.append(self) #add article to magazine articles

        self.author._magazines.append(self.magazine) #store magazines written
        self.author._articles.append(self) #add articles to author articles

    #Article property title
    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self,title):
        if hasattr(self,"_title"):
            raise Exception ("Title cannot change")
        elif isinstance(title,str) and 5 <= len(title) <= 50:
            self._title = title 
        else:
            raise Exception("Title must be a string of between 5 and 50 characters inclusive")

    #Article property author
    @property
    def author(self):
        return self._author 

    @author.setter
    def author (self,author):
        if isinstance(author,Author):
            self._author = author
        else:
            raise Exception ("Article author must be a author object")

    #Article property magazine
    @property
    def magazine(self):
        return self._magazine 

    @magazine.setter
    def magazine(self,magazine):
        if isinstance (magazine,Magazine):
            self._magazine = magazine
        else:
            raise Exception("Article magazine must be a magazine object")


class Author:
    def __init__(self, name):
        self.name = name 
        self._articles = []
        self._magazines = []
        
   #Author property name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if hasattr(self,"_name"):
            raise Exception ("Cannot change the name of the author")
        elif isinstance (name,str) and len(name) > 0:
            self._name = name
        else:
            raise Exception ("Name must be a string longer than 0 characters")

    #Author articles
    def articles(self):
        return [article for article in Article.all if article.author == self ]

    #Author magazines
    def magazines(self):
        contributed_mags = []
        for article in Article.all:
            if article.author == self:
                if article.magazine not in contributed_mags:
                    contributed_mags.append(article.magazine)
        return contributed_mags
    
    #Author add_article(magazine,title)
    def add_article(self, magazine, title):
        article = Article(self,magazine,title)
        self._articles.append(article)
        return article

    #Author topic_areas
    def topic_areas(self):
        mag_categories = []
        for article in self._articles:
            if article.author == self:
                if article.magazine.category not in mag_categories:
                    mag_categories.append(article.magazine.category)
        return mag_categories if mag_categories else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._authors = []
        self._articles = []

    #Magazine property name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance (name,str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string of between 2 and 16 characters inclusive")

    #Magazine property category
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self,category):
        if isinstance (category,str) and len(category) > 0:
            self._category = category
        else:
            raise Exception("Category must be a string longer than 0 characters")


    #Magazine articles
    def articles(self):
        return [article for article in Article.all if article.magazine == self] #list comprehension to filter articles
    
    #Magazine contributors
    def contributors(self):
        m_contributors = [] #store authors who contributed
        for article in Article.all:
            if article.magazine == self:
                if article.author not in m_contributors:
                    m_contributors.append(article.author)
        return m_contributors

    #Magazine article_titles
    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self ]
        return titles if titles else None


    #Magazine contributing authors
    def contributing_authors(self):
        pass
     
        