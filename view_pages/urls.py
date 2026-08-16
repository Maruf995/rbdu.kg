
from django.urls import path

from view_pages.views import history_page, law_page, main_page, department_page, readership_page, \
    services_page, vacancies_page, volunteer_page, contact_page, events_page, events_detail_page



urlpatterns = [
    path('', main_page, name='main-page'),
    path('history/', history_page, name='history-page'),
    path('departments/', department_page, name='department-page'),
    path('services/', services_page, name='services-page'),
    path('vacancies/', vacancies_page, name='vacancies-page'),
    path('law/', law_page, name='law-page'),
    path('volunteer/', volunteer_page, name='volunteer-page'),
    path('readership/', readership_page, name='readership-page'),
    path('contact/', contact_page, name='contact-page'), 
    path('events/', events_page, name='events_page'),
    path('events/<int:event_id>/', events_detail_page, name='events-detail-page'),
]