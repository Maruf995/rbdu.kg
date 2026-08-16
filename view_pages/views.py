from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from .models import Event

# Create your views here.
def main_page(request):
    return render(request, 'main-page.html')

def history_page(request):
    return render(request, 'history.html')

def department_page(request):
    return render(request, 'departments.html')

def services_page(request):
    return render(request, 'services.html')

def vacancies_page(request):
    return render(request, 'vacancies.html')

def law_page(request):
    return render(request, 'law.html')

def volunteer_page(request):
    return render(request, 'volunteer.html')

def readership_page(request):
    return render(request, 'readership.html')

def contact_page(request):
    return render(request, 'contact.html')


def events_page(request):
# Получаем уникальные даты, в которые есть мероприятия (возвращает список datetime.date)
    event_dates = Event.objects.dates('date', 'day').order_by('date')
    
    # Базовый QuerySet со всеми мероприятиями
    events = Event.objects.all().order_by('date')
    
    # Проверяем, есть ли фильтрация по дате в URL
    selected_date = request.GET.get('date')
    if selected_date:
        # Фильтруем мероприятия по конкретному дню
        events = events.filter(date__date=selected_date)

    context = {
        'events': events,
        'event_dates': event_dates,
        'selected_date': selected_date,
    }
    return render(request, 'events.html', context)

def events_detail_page(request, event_id):
    # Достаем мероприятие по ID или выдаем 404 страницу, если его нет
    event = get_object_or_404(Event, id=event_id)
    
    context = {
        'event': event,
    }
    return render(request, 'events_detail.html', context)