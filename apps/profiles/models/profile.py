from django.db import models

from apps import articles, authentication
from apps.core.models import TimeStampedAbstractModel


class Profile(TimeStampedAbstractModel):
    """ model that represent profile """
    user = models.OneToOneField(
        'authentication.User',
        on_delete=models.CASCADE,
    )
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False,
    )

    likes = models.ManyToManyField(
        'articles.Article',
        related_name='liked_by',
    )

    def __str__(self) -> str:
        return self.user.username
