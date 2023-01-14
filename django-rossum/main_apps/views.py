from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View

# from main_apps.listingitem import *
from .program import *


class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get_context_data(self):
        context = {
            'title': 'Home',
        }
        return context

class ProgramView(View):
    template_name = "pages/program.html"

    def get(self, request):
        
        # Mengambil input dari form
        return render(request, self.template_name)

    def post(self, request):
        ram = request.POST['ram']
        vga = request.POST['vga']
        # processor = request.POST['processor']
        # mobo = request.POST['mobo']
        # psu = request.POST['psu']
        # cooling = request.POST['cooling']
        
        computer = Computer(vga, ram)
        price = computer.sum_price()

        # Menambahkan hasil ke context data
        context = {
            "vga" : vga,
            "ram" : ram,
            "price": price
        }

        return render(request, self.template_name, context=context)

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
