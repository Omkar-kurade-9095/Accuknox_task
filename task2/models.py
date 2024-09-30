import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, **kwargs):
    print(f"[Signal] Signal triggered for instance: {instance.name}")
    print(f"[Signal] Running in thread: {threading.current_thread().name} (Thread ID: {threading.get_ident()})")
