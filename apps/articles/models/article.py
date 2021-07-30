from django.db import models

from apps import articles, profiles
from apps.core.models import TimeStampedAbstractModel


class Article(TimeStampedAbstractModel):
    """ A model that represent article"""
    title = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(db_index=True, max_length=200, unique=True)

    abstract = models.TextField()
    text = models.TextField()

    author = models.ForeignKey(
        'profiles.Profile',
        on_delete=models.CASCADE,
        related_name='articles',
    )
    tags = models.ManyToManyField(
        'articles.Tag',
        related_name='articles'
    )

    def __str__(self) -> str:
        return self.title
