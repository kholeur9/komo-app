from django.db.models.signals import post_save, post_delete
from .models import ForfaitClient, CreditClient, Client
from django.dispatch import receiver
from django.db.models import Sum

@receiver(post_save, sender=ForfaitClient)
def calcul_credit(sender, instance, created, **kwargs):
    if created:
        client = instance.numero_client
        forfait = instance.forfait_client
        credit_obtenu = forfait * 0.05

        CreditClient.objects.create(client=client, credit=credit_obtenu, forfait_client=instance)

@receiver([ post_save, post_delete ], sender=CreditClient)
def somme_credit(sender, instance, **kwargs):

    client = instance.client
    total_credit = CreditClient.objects.filter(client=client).aggregate(Sum('credit'))['credit__sum']
    client.total_credit = total_credit or 0
    client.save()
    