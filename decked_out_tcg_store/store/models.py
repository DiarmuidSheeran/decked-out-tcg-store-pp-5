from django.db import models

# Create your models here.
class SlideshowImage(models.Model):
    image = models.ImageField(upload_to='slideshow_images/')
    link = models.URLField()
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.alt_text