from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('allergies/', views.AllergiesListView.as_view()),
    path('components/', views.ComponentsListView.as_view()),
    path('components/<int:pk>', views.ComponentsDetailView.as_view()),
    path('analysis/<int:pk>', views.AnalysisDetailView.as_view()),
    path('analysis/', views.AnalysisListView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)