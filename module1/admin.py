from django.contrib import admin

# Register your models here.
from .models import Transaction,User,Bank,Account
admin.site.register(Transaction)
admin.site.register(User)
admin.site.register(Bank)
admin.site.register(Account)