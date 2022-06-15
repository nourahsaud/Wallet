from dataclasses import field
from rest_framework import serializers
from .models import Income, Expense, Plan, Consult


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
  
class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'