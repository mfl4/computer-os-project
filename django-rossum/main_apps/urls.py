from django.urls import path
from .views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("program/", ProgramView.as_view(), name="program"),
    path("history/", HistoryView.as_view(), name="history"),
    path("about/", AboutView.as_view(), name="about"),
]
