from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
    


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, default='general',on_delete=models.CASCADE)
    tags = TaggableManager()


    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.task_name
    
    
