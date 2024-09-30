import time
from django.core.management.base import BaseCommand
from task1.models import MyModel

class Command(BaseCommand):
    help = 'Test if signals are executed synchronously'

    def handle(self, *args, **kwargs):
        start_time = time.time()
        print("[Caller] Creating instance...")
        instance = MyModel.objects.create(name="Original Name", age=30)
        print(f"[Caller] Instance created: {instance.name}")
        end_time = time.time()

        total_time = end_time - start_time
        print(f"[Caller] Total time taken: {total_time:.2f} seconds")
