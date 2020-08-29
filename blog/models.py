from django.db import models


class DomainEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DomainEntity):
    name = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Article(DomainEntity):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='article_category')
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='article')

    def __str__(self):
        return self.title
