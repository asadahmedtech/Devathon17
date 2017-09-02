from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
PROBLEM_TYPES = (('a','a'),('b','b'))
COUNCILIDLIST = (('AC','AC'),('HK','HK'))
class problemPost(models.Model):
    rollNumber = models.CharField(max_length = 10)
    problemType = models.CharField(max_length = 100, choices = PROBLEM_TYPES, default = 'a')
    detail = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length = 10,default = '')
    councilMem = models.CharField(max_length = 30, default = '')
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.problemType
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    councilID = models.CharField(max_length = 10, choices = COUNCILIDLIST, default = None)

    def __str__(self):
        return str(self.user.username)
