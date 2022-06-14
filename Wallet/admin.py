from django.contrib import admin
from .models import Expense, Income, Plan
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('Amount', 'Category', 'Date')
    list_filter = ('Amount', 'Category', 'Date')
    search_fields = ('Category',)
    empty_value_display = '-empty-'

    list_per_page = 5

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('Amount', 'Source', 'Date')
    list_filter = ('Amount', 'Source', 'Date')
    search_fields = ('Source',)
    empty_value_display = '-empty-'

    list_per_page = 5

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
