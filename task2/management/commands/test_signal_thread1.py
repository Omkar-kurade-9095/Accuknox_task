import threading
from django.core.management.base import BaseCommand
from task2.models import MyModel

class Command(BaseCommand):
    help = 'Test if signals run in the same thread as the caller'

    def handle(self, *args, **kwargs):
        print(f"[Caller] Creating instance in thread: {threading.current_thread().name} (Thread ID: {threading.get_ident()})")
        instance = MyModel.objects.create(name="Original Name", age=30)
        print(f"[Caller] Instance created: {instance.name}")
