# -*- coding: utf-8 -*-
# czat/models.py

from django.db import models
from django.contrib.auth.models import User


class Wiadomosc(models.Model):

    """Klasa reprezentująca wiadomość w systemie"""
    tekst = models.CharField('treść wiadomości', max_length=300)
    data_pub = models.DateTimeField('data publikacji', auto_now_add=False)
    autor = models.ForeignKey(User)

    class Meta:  
        verbose_name = u'wiadomość'  
        verbose_name_plural = u'wiadomości'  
        ordering = ['data_pub']  

    def __str__(self):
        return self.tekst  
