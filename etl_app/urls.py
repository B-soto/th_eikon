from django.urls import path
from . import views

urlpatterns = [
    path("trigger_etl", views.trigger_etl, name="trigger_etl"),
    path("etl_job", views.etl_job, name="etl_job"),
]