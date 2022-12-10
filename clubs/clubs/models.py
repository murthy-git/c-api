from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    description = models.TextField(max_length=300, blank=False)
    created_by = models.CharField(max_length=10, blank=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

