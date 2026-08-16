from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    
    # Это главные фото (обложка статьи и картинка для карточки)
    image = models.ImageField(upload_to='events/')
    mini_image = models.ImageField(upload_to='events/mini/', null=True, blank=True)

    def __str__(self):
        return self.title


# НОВАЯ МОДЕЛЬ ДЛЯ ГАЛЕРЕИ
class EventImage(models.Model):
    # Связываем фото с конкретным мероприятием
    # related_name='images' позволит нам в HTML обращаться к фото как event.images.all
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    
    # Само поле для загрузки фото галереи
    image = models.ImageField(upload_to='events/gallery/')
    
    def __str__(self):
        return f"Фото для: {self.event.title}"