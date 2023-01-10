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
        return render(request, self.template_name)

    def post(self, request):
        # Mengambil input dari form
        ram = request.POST['ram']
        vga = request.POST['vga']
        # processor = request.POST['processor']
        # mobo = request.POST['mobo']
        # psu = request.POST['psu']
        # cooling = request.POST['cooling']
        
        print(vga)
        print(ram)
        # print(processor)
        # print(mobo)
        # print(psu)
        # print(cooling)
        computer = Computer(vga, ram)
        price = computer.sum_price()
        print(price)

        context = {
            "vga" : vga,
            "ram" : ram,
            "price": price
        }

        # Menambahkan hasil ke context data
        return render(request, self.template_name, context=context)

    # def post(request):
    #     context = {
    #         "vga": request.post["vga"],
    #         "ram": request.post["ram"]
    #         "processor": processor,
    #         "mobo": mobo,
    #         "psu": psu,
    #         "cooling": cooling,
    #         "price" : price
    #         'data' : take_data()
    #     }

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
