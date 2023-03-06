from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering=('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name  

class Item(models.Model):
    category=models.ForeignKey(Category,related_name='items', on_delete=models.CASCADE , verbose_name='Категорія')
    name=models.CharField(max_length=255 , verbose_name='Назва')
    discription=models.TextField(blank=True, null=True , verbose_name='Опис')
    price=models.FloatField(verbose_name='Вартість')
    image = models.ImageField(upload_to='item_images',blank=True,null=True , verbose_name='Фото')
    is_sold = models.BooleanField(default=False , verbose_name='Продано')
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
