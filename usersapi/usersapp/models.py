from django.db import models

# Create your models here.


class User(models.Model):

    class Meta:

        db_table = 'user'

    id = models.UUIDField(primary_key=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
