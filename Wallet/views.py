from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
#from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework import mixins, viewsets

from .models import Expense, Income, Plan
from .serializers import ExpenseSerializer, IncomeSerializer, PlanSerializer

global Balance

# Create your views here.

# List == GET
# Create == POST
# pk Query == GET 
# Update == PUT
# Delete == DELETE

# Expense 
# GET | POST
@api_view(['GET', 'POST'])
def expenses_view(request):
    # GET
    if request.method == 'GET':
        expense = Expense.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def expenses_view_pk(request,pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        expense.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# Income 
# GET | POST
@api_view(['GET', 'POST'])
def income_view(request):
    # GET
    if request.method == 'GET':
        income = Income.objects.all()
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def income_view_pk(request,pk):
    try:
        income = Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = IncomeSerializer(income)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        income.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


