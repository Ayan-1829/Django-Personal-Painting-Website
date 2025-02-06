from django.db import models

# Create your models here.

class Painting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='paintings/')
    MEDIUM_CHOICES = [
        ('Acrylic on Canvas', 'Acrylic on Canvas'),
        ('Oil Painting', 'Oil Painting'),
        ('Watercolor', 'Watercolor'),
        ('Pencil Sketch', 'Pencil Sketch'),
        ('Charcoal Drawing', 'Charcoal Drawing'),
        ('Mixed Media', 'Mixed Media'),
    ]
    
    medium = models.CharField(max_length=50, choices=MEDIUM_CHOICES, default='Acrylic on Canvas')

    def __str__(self):
        return self.title
