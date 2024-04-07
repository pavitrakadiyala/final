from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    account_number = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.IntegerField(unique=True)
    balance = models.IntegerField()
    transaction_id= models.IntegerField()

    def __str__(self):
        return f"Account {self.account_number} - Balance: {self.current_balance}"

# class Transaction(models.Model):
#     TRANSACTION_TYPES = (
#         ('CREDIT', 'Credit'),
#         ('DEBIT', 'Debit'),
#     )

#     account = models.ForeignKey(Account, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
#     note = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)