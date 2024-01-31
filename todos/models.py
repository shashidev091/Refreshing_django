from django.db import models

# Create your models here.


class Todo(models.Model):
    TASK_STATUSES = {
        "C": "Completed",
        "P": "Pending",
        "IP": "In Progress",
        "TP": "Task Postponded",
        "D": "Task Deleted",
        "F": "Failed"
    }
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    progress = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    completed_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)
    status = models.CharField(max_length=2, choices=TASK_STATUSES)

    def __str__(self):
        return f"title: {self.title}, description: {self.description}, progress: {self.progress}, status: {self.status}, created_at: {self.created_at}, update_at: {self.updated_at}, completed_at: {self.completed_at}"
