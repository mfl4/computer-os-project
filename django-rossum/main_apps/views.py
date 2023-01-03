from django.views.generic.base import TemplateView
# from .program import *

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get_context_data(self):
        context = {
            'title': 'Home',
        }
        return context

class ProgramView(TemplateView):
    template_name = "pages/program.html"
    
    def get_context_data(self):
        context = {
            'title': 'Program',

        }
        return context

class HistoryView(TemplateView):
    template_name = "pages/history.html"
    
    def get_context_data(self):
        context = {
            'title': 'History',
        }
        return context

class AboutView(TemplateView):
    template_name = "pages/about.html"
    
    def get_context_data(self):
        context = {
            'title': 'About',
        }
        return context
