from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Mesure(models.Model):
    humidite = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
