from django.core.management.base import BaseCommand
from django.db import transaction
from task3.models import MyModel

class Command(BaseCommand):
    help = 'Test if signals run in the same transaction as the caller'

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                print("[Caller] Creating instance...")
                instance = MyModel.objects.create(name="Test Object")
                print(f"[Caller] Instance created with status: {instance.status}")

                # Force a rollback by raising an exception
                raise Exception("Forcing transaction rollback!")
        except Exception as e:
            print(f"[Caller] Exception occurred: {e}")

        # Check if any instance was saved despite the rollback
        instance_count = MyModel.objects.count()
        print(f"[Caller] Total instances in DB after rollback: {instance_count}")
