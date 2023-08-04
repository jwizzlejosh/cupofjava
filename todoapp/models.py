from django.db import models

# Create your models here.

# TodoListItem
class TodoListItem(models.Model):
    content = models.TextField() 

