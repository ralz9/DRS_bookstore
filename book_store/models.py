
# from django.db import models
#
# # Create your models here.
#
# class Owner(models.Model):
#     publisher = models.CharField(max_length=60 , verbose_name='Издатель')
#
#     def __str__(self):
#         return f'{self.publisher}'
#
#
#
# """
# Описываю модель в бд
# """
# class CustomUser(models.Model):
#     title = models.CharField(max_length=255)
#     descriptions = models.CharField(max_length=84, null=True, blank=True)
#     owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='books')
