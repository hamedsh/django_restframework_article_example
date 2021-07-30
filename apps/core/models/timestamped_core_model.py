from django.db import models


class TimeStampedAbstractModel(models.Model):
    """ A Base Model to Esase of creation models with timestamp"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
