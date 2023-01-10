from django.views.generic.base import TemplateView
from django.shortcuts import render
from .program import *

class IndexView(TemplateView):
    template_name = "pages/index.html"
    
    def get_context_data(self):
        context = {
            'title': 'Home',
        }
        return context

class ProgramView(TemplateView):
    template_name = "pages/program.html"

    def post(self, request):
        # Mengambil input dari form
        processor = request.POST['processor']
        memory = request.POST['memory']
        hard_drive = request.POST['hard_drive']
        graphics_card = request.POST['graphics_card']
        
        print(processor)
        print(memory)
        print(hard_drive)
        print(graphics_card)
        computer = Computer(processor, memory, hard_drive, graphics_card)
        price = computer.sum_price()

        # Menambahkan hasil ke context data
        context = {
            "processor": processor,
            "memory": memory,
            "hard_drive": hard_drive,
            "graphics_card": graphics_card,
            "price": price
            }
        return render(self.template_name, context)

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
