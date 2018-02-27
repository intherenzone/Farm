from django.db import models

# Create your models here.
REGIONS = (
    ('NE US', 'NE US'),
    ('SE US', 'SE US'),
    ('NW US', 'NW US'),
    ('SW US', 'SW US'),
)
class Farm(models.Model):
    name = models.CharField(("Farm Name"), max_length=255)
    region = models.CharField(("Region of Farm"), max_length=255, blank=True, null=True, choices=REGIONS)
