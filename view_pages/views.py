from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    return render(request, 'main-page.html')