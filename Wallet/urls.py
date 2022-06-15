from django import views
from django.urls import path, include
from pkg_resources import DefaultProvider
from . import views

app_name = 'wallet'
urlpatterns = [
    # Exoenses Endpoints
    path('expense/', views.expenses_view, name='list expenses'),
    path('expense/add', views.expenses_view, name='add expense'),
    path('expense/<int:pk>',views.expenses_view_pk, name='view expense'),
    path('expense/update/<int:pk>',views.expenses_view_pk, name='update expense'),
    path('expense/delete/<int:pk>',views.expenses_view_pk, name='delete expense'),

    # Income Endpoints
    path('income/', views.income_view, name='list income'),
    path('income/add', views.income_view, name='add income'),
    path('income/<int:pk>',views.income_view_pk, name='view income'),
    path('income/update/<int:pk>',views.income_view_pk, name='update income'),
    path('income/delete/<int:pk>',views.income_view_pk, name='delete income'),

    # Summary Endpoints
    # Expenses
    path('expense/summary', views.expense_summary, name='expenses summary'),
    # Income
    path('income/summary', views.income_summary, name='income summary'),

    # Plan Endpoints
    path('plan/', views.plan_view, name='list plans'),
    path('plan/add', views.plan_view, name='add plan'),
    path('plan/<int:pk>',views.plan_view_pk, name='view plan'),
    path('plan/update/<int:pk>',views.plan_view_pk, name='update plan'),
    path('plan/delete/<int:pk>',views.plan_view_pk, name='delete plan'),

    # Consult Endpoints
    path('consult/', views.plan_view, name='view consult'),
    path('consult/add', views.plan_view, name='add consult'),

]