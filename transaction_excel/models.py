from django.db import models

# Create your models here.
class ExcelInput(models.Model):
  extract_data = models.FileField(upload_to='extract_data/')
  # extract_data = models.FileField(upload_to='extract_data/')