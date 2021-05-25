from django.db import models


# Create your models here.
class Member(models.Model):
    TEA = 'tea'
    COFFEE = 'coffee'
    PREFERS = [
        (TEA, ('Prefers tea')),
        (COFFEE, ('Prefers coffee')),
    ]

    name = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    prefers = models.CharField(
        max_length=32,
        choices=PREFERS,
        default=TEA,
    )

    def __str__(self):
        return self.name
