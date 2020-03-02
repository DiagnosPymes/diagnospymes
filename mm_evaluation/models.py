from django.db import models

# Create your models here.
"""This table contains the information regarding specific practices, which are directly related to each level of each process and are used to describe the behaviour of a certain level in each process."""
class SpecificPractice(models.Model):

    """Description is a text field which contains a brief explanations of a particular specific practice."""
    description = models.CharField(max_length = 500)
    """Recommendation is a text which tells you how to achieve the level of this specific practice."""
    recommendation = models.CharField(max_length = 500)
    """Process_id is a foreign key, which relates this specific practice to its corresponding process."""
    process_id = models.IntegerField()
    """Score is the level of process this specific practive is related to, it is a number between 0 and 5."""
    score = models.IntegerField()

    class Meta:
        db_table = 'specific_practice'

"""This table contains the information regarding general practices, which are related to global levels of performance and are used to describe briefly the behaviour of a PYME in a given level."""        
class GeneralPractice(models.Model):

    """Description is a text field which contains a brief explanations of a particular general practice."""
    description = models.CharField(max_length = 500)
    """Recommendation is a text which tells you how to achieve the level of this general practice."""
    recommendation = models.CharField(max_length = 500)
    """Score is the level of overall logistic performance this specific practive is related to, it is a number between 0 and 5."""
    score = models.IntegerField()
    
    class Meta:
        db_table = 'general_practice'

"""This table contains the information regardin the different macroprocesses relevant to the self-evaluation process, which are 10 and describe the large areas of concern when it comes to logistical performance."""        
class Macroprocess(models.Model):

    """Description is a text field which contains a brief explanations of a particular macroprocess."""
    description = models.CharField(max_length = 500)
    """Name contains the macroprocess' high level name."""
    name = models.CharField(max_length = 50)

    class Meto:
        db_table = 'macroprocess'
