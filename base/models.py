from django.db import models

# Create your models here.
class RoomMember(models.Model):
    name = models.CharField(max_length=255)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Room Member'
        verbose_name_plural = 'Room Members'