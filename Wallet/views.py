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
from rest_framework_simplejwt.authentication import JWTAuthentication
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def expenses_view(request):
    # GET
    if request.method == 'GET':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.expenses_view'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        expense = Expense.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return Response(serializer.data)
    
    # POST
    elif request.method == 'POST':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.expenses_view'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def expenses_view_pk(request,pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':

        if not request.user.is_authenticated or not request.user.has_perm('wallet.expenses_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.expenses_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.expenses_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        expense.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# Income 
# GET | POST
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def income_view(request):
    # GET
    if request.method == 'GET':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.income_view'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        income = Income.objects.all()
        serializer = IncomeSerializer(income, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.income_view'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def income_view_pk(request,pk):
    try:
        income = Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.income_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = IncomeSerializer(income)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.income_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        serializer = IncomeSerializer(income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        if not request.user.is_authenticated or not request.user.has_perm('wallet.income_view_pk'):
            return Response("Not Allowed", status = status.HTTP_400_BAD_REQUEST)
        
        income.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)