from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class RoomRequest(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_file = models.FileField(upload_to='plans/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заявка от {self.user.username} - {self.created_at}'
