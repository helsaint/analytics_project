from django.db import models

# Create your models here.
class Cities2(models.Model):
    index = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'cities2_cities2'