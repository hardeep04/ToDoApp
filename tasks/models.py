from django.db import models
from django.db import IntegrityError

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        # If the task is being marked as complete, delete it instead of saving
        if self.complete:
            try:
                # Delete the task if complete
                self.delete()
            except IntegrityError:
                pass  # Handle any exceptions if necessary
        else:
            super().save(*args, **kwargs)


    def __str__(self):
        return self.title
