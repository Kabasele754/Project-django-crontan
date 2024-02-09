from django.db import models

# Create your models here.


class Notification(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    recipient = models.EmailField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

