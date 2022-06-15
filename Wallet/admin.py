from django.contrib import admin
from .models import Consult, Expense, Income, Plan
# Register your models here.

# Customize the expenses admin interface
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'category', 'date')
    list_filter = ('amount', 'category', 'date')
    search_fields = ('category',)
    empty_value_display = '-empty-'

    list_per_page = 5
# Customize the income admin interface
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('amount', 'source', 'date')
    list_filter = ('amount', 'source', 'date')
    search_fields = ('source',)
    empty_value_display = '-empty-'

    list_per_page = 5

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Plan)
admin.site.register(Consult)
