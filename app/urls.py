from django.urls import path
from . import views


urlpatterns = [
    path('', views.input_form, name='input_form'),
    path('analysis/<int:instance_id>/', views.analysis, name='analysis'),
]