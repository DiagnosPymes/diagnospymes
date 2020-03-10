from django.urls import path

from . import views


app_name = 'mm_evaluation'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('autoevaluacion/', views.Autoevaluation.as_view(), name='autoevaluacion'),
    path('resultados/', views.PreviousResults.as_view(), name='resultados'),
    path('resultados/<int:pk>/', views.ResultDetail.as_view(), name='detalleResultado' )
    path('autoevaluation/', views.Autoevaluation.as_view()),
]
