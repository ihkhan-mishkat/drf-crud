from django.db import models

class Contactlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    phone = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)
