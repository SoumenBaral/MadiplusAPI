from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    image = models.ImageField( upload_to="service/images/")

    def __str__(self) -> str:
        return self.name
    