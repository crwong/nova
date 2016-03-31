from __future__ import unicode_literals

from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=256)

class Interviewer(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    level = models.CharField(max_length=256)
    skills = models.ManyToManyField(Skill)

class Interview(models.Model):
    time = models.DateTimeField()
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    candidate = models.CharField(max_length=256)
