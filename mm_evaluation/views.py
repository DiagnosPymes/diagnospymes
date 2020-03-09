from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Process, Macroprocess, Autoevaluation
from django.views.generic.list import ListView 

class Autoevaluation(ListView):
    model = Macroprocess
    template_name = 'mm_evaluation/autoevaluation.html'
    context_object_name = 'macroprocesses_list'

    #def get_context_data(self, **kwargs):
    #    # Call the base implementation first to get a context
    #    context = super().get_context_data(**kwargs)
    #    # Add in a QuerySet of all the books
    #    context['process_list'] = Process.objects.all()
    #    return context

class PreviousResults(ListView):
    model = Autoevaluation
    template_name = 'mm_evaluation/previousresults.html'
    context_object_name = 'all_previous_results'

    def get_query(self):
        return Autoevaluation.objects.filter(PYME_id=1,final_score__isnull=False).order_by('last_time_edition')
