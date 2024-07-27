from django.db import models


class Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    username = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    time_register = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    data_born = models.DateField()
    content = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.username



