from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class MyUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.username

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'new'),
        ('IN PROGRESS', 'in progress'),
        ('DONE', 'done'),
        ('INVALID', 'invalid'),
        ]
    title=models.CharField(max_length=240)
    post_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    open_user = models.ForeignKey(MyUser,on_delete=models.CASCADE,related_name="open_user")
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default='NEW',
    )
    user_assigned = models.ForeignKey(MyUser,on_delete=models.CASCADE, default=None,related_name="assigned_user",null=True)
    user_completed = models.ForeignKey(MyUser,on_delete=models.CASCADE, default=None,related_name="completed_user",null=True)
    def __str__(self):
        return self.title
        
class Author(models.Model):
    pass