from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField()
    image = models.ImageField(upload_to="service/images/",
            validators=[FileExtensionValidator
            (allowed_extensions=['jpg', 'jpeg', 'png'])]
)