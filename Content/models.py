from django.db import models


# Create your models here.
class Ads(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='contents', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ads'