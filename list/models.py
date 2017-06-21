from django.db import models

# Create your models here.


class TodoList(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def is_completed(self):
        return self.completed

    def get_name(self):
        return name
