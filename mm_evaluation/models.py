from django.db import models

# Create your models here.
class SpecificPractice(models.Model):
    description = models.CharField(max_length = 500)
    recommendation = models.CharField(max_length = 500)
    process_id = models.IntegerField()
    score = models.IntegerField()

    class Meta:
        db_table = 'specific_practice'

        
class GeneralPractice(models.Model):
    description = models.CharField(max_length = 500)
    recommendation = models.CharField(max_length = 500)
    score = models.IntegerField()
    
    class Meta:
        db_table = 'general_practice'

        
class Macroprocess(models.Model):
    description = models.CharField(max_length = 500)
    name = models.CharField(max_length = 50)

    class Meto:
        db_table = 'macroprocess'
