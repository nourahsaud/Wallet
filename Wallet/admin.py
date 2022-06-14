from django.contrib import admin
from .models import Expense, Income, Plan
# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'category', 'date')
    list_filter = ('amount', 'category', 'date')
    search_fields = ('category',)
    empty_value_display = '-empty-'

    list_per_page = 5

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'description', 'Source', 'date')
    list_filter = ('amount', 'Source', 'date')
    search_fields = ('Source',)
    empty_value_display = '-empty-'

    list_per_page = 5

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Plan)
