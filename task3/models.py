from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Pending")

@receiver(post_save, sender=MyModel)
def update_status(sender, instance, **kwargs):
    print(f"[Signal] Signal triggered. Updating status for instance: {instance.name}")
    instance.status = "Processed"
    instance.save()  # Updating the status field
