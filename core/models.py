from django.db import models
from django.contrib.auth.models import User



# Create your models here.




class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bank(models.Model):
    bank_name = models.CharField(max_length=32, default="Generic bank name")
    address = models.CharField(max_length=32, default="Generic Bank Address")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.bank_name
    

class Currency(models.Model):
    currency_name=models.CharField(max_length=16, default="Generic currency name")
    shor_name = models.CharField(max_length=3, default="GC")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.currency_name


class AccountBank(models.Model):
    account_name=models.CharField(max_length=16, default="Generic account")
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.account_name
    

class CategoryProvider(models.Model):
    category_name=models.CharField(max_length=16, default="Generic category name")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.category_name
    

class Provider(models.Model):
    provider_name=models.CharField(max_length=32, default="Generic provider name")
    category=models.ForeignKey(CategoryProvider, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.provider_name
    

class Payment(models.Model):
    payment_name=models.CharField(max_length=32, default="Generic payment name")
    timestamp = models.DateField(auto_now_add=True)
    account=models.ForeignKey(AccountBank, on_delete=models.CASCADE)
    provider=models.ForeignKey(Provider, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.payment_name




