from django.db import models

DEFAULT_STATUS = 'draft'

STATUS = [
    ('draft', 'Taslak'),
    ('publihsed', 'Yayinlandi'),
    ('deleted', 'Silindi'),
]

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default='',
    )
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='page',
        blank=True,
        null=True
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(
        upload_to='page',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title