from django.core.exceptions import ValidationError
from django.db import models


class TimeBaseModel(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ImageBaseModel(TimeBaseModel):
    IMAGE_TYPE = (
        ('portrait', 'Portrait'),
        ('landscape', 'Landscape'),
    )

    image_type = models.CharField(max_length=10, choices=IMAGE_TYPE)
    image = models.ImageField(upload_to='productapp_images')
    is_default = models.BooleanField(default=False)

    def clean(self):
        if self.image_type == 'portrait':
            if self.image.width > self.image.height:
                raise ValidationError('Image must be portrait')
        elif self.image_type == 'landscape':
            if self.image.width < self.image.height:
                raise ValidationError('Image must be landscape')

        if self.image.size > 1024 * 1024:
            raise ValidationError('Image size must be less than 1MB')

        if self.image.name.split('.')[-1] != 'png':
            raise ValidationError('Image must be PNG')

    class Meta:
        abstract = True
