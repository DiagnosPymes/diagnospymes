from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View, DetailView
from .models import Process, Macroprocess
from .models import Autoevaluation as AutoevaluationModel
from django.template.loader import render_to_string

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
    template_name = 'mm_evaluation/previousresults.html'
    context_object_name = 'all_previous_results'

    def get_queryset(self):
        return AutoevaluationModel.objects.filter(pyme_id_id=1,final_score__isnull=False).order_by('last_time_edition')

class ResultDetail(DetailView):
    model = AutoevaluationModel
    template_name = 'mm_evaluation/resultdetail.html'
    
    
class IndexView(View):
    template_name = 'mm_evaluation/index.html'
    context_object_name = 'general_list'

    def get(self, request, *args, **kwargs):
        return HttpResponse(render_to_string(self.template_name))

