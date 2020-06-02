from django import template
from mm_evaluation.models import Answer, Process, Autoevaluation

register = template.Library()

@register.filter
def get_score(p, a):
    try:
        prefix = "Puntaje actual: "
        score =  str(Answer.objects.get(autoevaluation=a,process=p).score)
    except Answer.DoesNotExist:
        prefix = "Sin responder"
        score = ""
    return (prefix, score)
