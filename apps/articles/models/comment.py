from django.db import models

from apps import articles
from apps.core.models import TimeStampedAbstractModel


class Comment(TimeStampedAbstractModel):
    """ Model that represent Comments """
    text = models.TextField()

    article = models.ForeignKey(
        'articles.Article',
        related_name='comments',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        'profiles.Profile',
        related_name='comments',
        on_delete=models.CASCADE,
    )
