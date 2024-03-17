from django.db import models

# Create your models here.
class course_enrollment(models.Model):
    SID = models.TextField(u'SID')
    CID = models.TextField(u'CID')
    midScore = models.FloatField(u'midScore')
    finalScore = models.FloatField(u'finalScore')
    Score = models.FloatField(u'Score')
