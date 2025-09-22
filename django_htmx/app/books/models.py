from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    author = models.CharField(max_length=200, verbose_name=_('Author'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    read = models.BooleanField(default=False, verbose_name=_('Read'))

    def __str__(self):
        return self.title
