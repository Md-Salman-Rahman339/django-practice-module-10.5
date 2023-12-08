from django.db import models
from taskcategory.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    tasktitle=models.CharField(max_length=50)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    task_assign_date=models.DateField()
    categories = models.ManyToManyField(TaskCategory)


    def __str__(self):
        return self.tasktitle
    