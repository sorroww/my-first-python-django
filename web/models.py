# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return 'in this date my expense is ::::{}---{}'.format(self.date, self.amount)
class Income(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    date = models.DateTimeField()
    def __unicode__(self):
        return 'at this moment my income is :: {}---{}'.format(self.date, self.amount)    
