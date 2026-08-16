from django.contrib import admin
from .models import Event, EventImage

admin.site.site_header = "Административная панель РБДУ"
admin.site.index_title = "Добро пожаловать в административную панель РБДУ"
admin.site.site_title = "Административная панель РБДУ"

# Создаем класс-вставку для галереи
class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3  # Количество пустых полей для загрузки фото, которые будут отображаться сразу

# Настраиваем админку для Event
class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline] # Подключаем нашу галерею внутрь мероприятия

# Регистрируем модель Event, передавая ей настройки EventAdmin
admin.site.register(Event, EventAdmin)
admin.site.register(EventImage)