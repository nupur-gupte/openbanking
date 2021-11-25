from django.db import models

# Create your models here.
class User(models.Model):
	user_id=models.AutoField
	firstname=models.CharField(max_length=20)
	lastname=models.CharField(max_length=20)
	email=models.CharField(max_length=50)
	age=models.IntegerField()
	income=models.FloatField(default=0)

	def __str__(self):
		return self.firstname

class Bank(models.Model):
	ifscode=models.CharField(max_length=25)
	bank_name=models.CharField(max_length=50)

	def __str__(self):
		return self.bank_name

class Account(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,default=0)
	bank=models.ForeignKey(Bank,on_delete=models.CASCADE)
	accno=models.CharField(max_length=20,default=0)
	branch=models.CharField(max_length=20)
	balance=models.FloatField(default=0)

	def __str__(self):
		return self.accno

class Transaction(models.Model):
	#user=models.ForeignKey(User,on_delete=models.CASCADE)
	txn_id=models.AutoField
	acc=models.ForeignKey(Account,on_delete=models.CASCADE,default=0)
	category_name=models.CharField(max_length=50)
	desc=models.CharField(max_length=300)
	date=models.DateField()
	price=models.FloatField(default=0)
	# balance=models.IntegerField(default=0)
	@property
	def bal(self):
		self.acc.balance=self.acc.balance-self.price
		return self.acc.balance
	
	def __str__(self):
		return self.category_name
