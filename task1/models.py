import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

@receiver(post_save, sender=MyModel)
def my_model_saved(sender, instance, **kwargs):
    print(f"[Signal] Signal triggered for instance: {instance.name}")
    print("[Signal] Simulating long task...")
    time.sleep(5)  # Simulate a long task by sleeping for 5 seconds
    print("[Signal] Signal processing completed")
