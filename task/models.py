from django.db import models
from category.models import CategoryModel

class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(CategoryModel, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
