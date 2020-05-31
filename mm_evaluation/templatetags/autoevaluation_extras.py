from django import template
from mm_evaluation.models import Answer, Process, Autoevaluation

register = template.Library()

@register.filter
def get_score(p, a):
    try:
        score = "Puntaje actual: " + str(Answer.objects.get(autoevaluation=a,process=p).score)
    except Answer.DoesNotExist:
        score = "Sin responder"
    return score
