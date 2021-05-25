from django.db import models

# Create your models here.
class Tea(models.Model):
    title = models.CharField(max_length=32)
    kind = models.CharField(max_length=12)
    price = models.FloatField()
    image = models.ImageField(upload_to='tea_images', blank=True)

    def __str__(self):
        return self.title