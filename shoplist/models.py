from django.db import models
from django.contrib.auth.models import User

class Shoplist(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Items(models.Model):
    item = models.CharField(max_length=100)
    datecompleted = models.DateTimeField(null=True, blank=True)
    shoplist = models.ForeignKey(Shoplist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
