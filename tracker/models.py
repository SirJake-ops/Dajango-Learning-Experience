from django.db import models

from application_user.Base import BaseEntity


class Bug(BaseEntity):
    name = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    project = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    resolved_date = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        data = {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "project": self.project,
            "assigned_to": self.assigned_to,
            "created_by": self.created_by,
            "resolved_date": self.resolved_date,
        }
        return data
