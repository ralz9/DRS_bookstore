from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CustomUser(models.Model):
    title = models.CharField(max_length=128, blank=True)
    descriptions = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book', verbose_name='Владелец поста')
    image = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return f'{self.title}'
