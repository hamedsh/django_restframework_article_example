from django.db import models

from apps.core.models import TimeStampedAbstractModel


class Tag(TimeStampedAbstractModel):
    tag = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self) -> str:
        return self.tag
