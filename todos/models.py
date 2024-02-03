from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6, validators=[
                                   MinLengthValidator(limit_value=6)])
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"street: {self.street}, postal_code: {self.postal_code}, country: {self.country}, city: {self.city}"


class Author(models.Model):
    first_name = models.CharField(max_length=10, validators=[
                                  MinLengthValidator(limit_value=3)])
    last_name = models.CharField(max_length=10, validators=[
                                 MinLengthValidator(limit_value=3)])
    email = models.EmailField(unique=True)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, email: {self.email}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


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
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="todos")

    def __str__(self):
        return f"title: {self.title}, description: {self.description}, progress: {self.progress}, status: {self.status}, created_at: {self.created_at}, update_at: {self.updated_at}, completed_at: {self.completed_at}"

    def get_absolute_url(self):
        return reverse("update-task", args=[self.id])
