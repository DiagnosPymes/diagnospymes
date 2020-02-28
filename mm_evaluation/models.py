from django.db import models

class Autoevaluation(models.Model):
    """pyme_id is the id of the PYME for whom the autoevaluation will be filled out. 'start_time' refers to when the autoevaluation had begun. 'last_time_edition' refers to the last edition time of the autoevaluation. 'final_score' refers to the final ponderation, when all macroprocesses have been filled out."""
    pyme_id = models.ForeignKey(PYME, on_delete=models.CASCADE)
    start_time = models.DateField()
    last_time_edition = models.DateField()
    final_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_1_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_2_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_3_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_4_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_5_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_6_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_7_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_8_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_9_score = models.DecimalField(max_digits=1, decimal_places=2)
    macroprocess_10_score = models.DecimalField(max_digits=1, decimal_places=2)


    class Meta:
        db_table = 'autoevaluation'


class Process(models.Model):
    """This is the database table where general information related to each process is stored. 'description' makes reference to the process sspecific description. Weight is needed when computing the macroprocess score. 'macroprocess_id' is the macroprocess to which the process belongs."""
    macroprocess_id = models.ForeignKey(Macroprocess, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    weight = models.IntegerField()


    class Meta:
        db_table = 'process'


class Answer(models.Model):
    """When a process is evaluated in an autoevaluation an entry in the 'answer' table will be created."""
    process_id = models.ForeignKey(Process, on_delete=models.CASCADE)
    autoevaluation_id = models.ForeignKey(Autoevaluation, on_delete=models.CASCADE)
    score = models.IntegerValue()


    class Meta:
        db_table = 'answer'
