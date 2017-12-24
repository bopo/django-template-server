from django.db.models.signals import pre_delete
from django.dispatch import receiver

from service.resource.models import Video


@receiver(pre_delete)
def pre_delete_handler(sender, instance, using, **kwargs):
    if isinstance(instance, Video):
        if instance.checker_runtime:
            instance.checker_runtime.delete()


pre_delete.connect(pre_delete_handler)
