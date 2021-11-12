from django.db import models

# Create your models here.


# HOSPITAL DATA BASE 

# auth group ------------ 1
class auth_group(models.Model):

    name = models.CharField(max_length=120)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
