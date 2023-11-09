from django.db import models

# Feedback models .

class Feedback(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    category = models.CharField(max_length=255)
    message = models.TextField()
    attachment = models.FileField(upload_to='feedback_attchments/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
