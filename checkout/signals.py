from django.db.Models.signals import post_save,post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, intance, created, **kwargs):
    ***
    Update order totel on Timeline update/created
    ***

    isinstance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, intance, **kwargs):
    ***
    Update order totel on Timeline delete
    ***

    isinstance.order.update_total()