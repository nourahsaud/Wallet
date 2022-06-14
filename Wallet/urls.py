from django import views
from django.urls import path, include
from pkg_resources import DefaultProvider
from . import views


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

]