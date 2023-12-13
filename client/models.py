# from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=9, null=True, blank=True, unique=True)
    total_credit = models.IntegerField(default=0)

    def total_credit(self):
        credits = CreditClient.objects.filter(client=self)
        total = sum(credit.credit for credit in credits)
        return total
    
    def __str__(self):
        return str(self.numero)

class ForfaitClient(models.Model):
    numero_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    forfait_client = models.IntegerField(default=0)
    date_Achat = models.DateField(default=0)
    
    def __str__(self):
        return str(self.forfait_client) + " - date: " + str(self.date_Achat)

class CreditClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    forfait_client = models.ForeignKey(ForfaitClient, on_delete=models.CASCADE)
    credit = models.IntegerField(default=0)
    date_credit = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.credit) + " - date: " + str(self.date_credit)