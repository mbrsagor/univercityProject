from django.contrib import admin
from blog.models.article import Category, Article
from blog.models.book import Publisher, Author, Book

admin.site.register(Category)
admin.site.register(Article)

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
