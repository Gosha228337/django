from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detal, name='detal'),
    path('<int:question_id>/results/',views.results, name='results'),
    path('<int:question_id>/vote/', views.voite, name='vote')
]