from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


__all__ = ['VCard']


class VCard(models.Model):
    name = models.CharField(max_length=64, verbose_name='Name')
    surname = models.CharField(max_length=64, verbose_name='Surname')
    birth_date = models.DateField(verbose_name='Birth Date')
    bio = models.TextField(blank=True, verbose_name='BIO')
    e_mail = models.EmailField(verbose_name='E-mail')
    photo = models.ImageField(upload_to='photo', blank=True)
    skype = models.CharField(max_length=64, blank=True, verbose_name='Skype')
    mob = models.CharField(max_length=64, blank=True, verbose_name='Mob.')
    jid = models.CharField(max_length=64, blank=True, verbose_name='JID')

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.surname)

