from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.TextField()
    image_url = models.URLField(max_length=2036)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True, null=True)

    def upgrade(self):
        self.update_date = timezone.now
        self.save()

    def __str__(self):
        return self.name

