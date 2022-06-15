import datetime
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status, response
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Expense, Income, Plan, Consult
from .serializers import ConsultationSerializer, ExpenseSerializer, IncomeSerializer, PlanSerializer


global Balance
global totalexpenses
global totalincome

# Create your views here.

# List == GET
# Create == POST
# pk Query == GET 
# Update == PUT
# Delete == DELETE

# index == GET --> balance, totalexpenses, totalincome
    

# Expense 
# GET | POST
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

# GET | The Points for the Expense summary
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def expense_summary(request):
    todays_date = datetime.date.today()
    one_months_ago = todays_date-datetime.timedelta(days=30)
    expense = Expense.objects.filter(date__gte=one_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category

    category_list = list(set(map(get_category, expense)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expense.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in expense:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return Response({'expense_category_data': finalrep}, status=status.HTTP_200_OK)

# Income 
# GET | POST
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
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

# GET | The Points for the Expense summary
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def income_summary(request):
    todays_date = datetime.date.today()
    one_months_ago = todays_date-datetime.timedelta(days=30)
    income = Income.objects.filter(date__gte=one_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_source(income):
        return income.source

    source_list = list(set(map(get_source, income)))

    def get_income_source_amount(source):
        amount = 0
        filtered_by_source = income.filter(source=source)

        for item in filtered_by_source:
            amount += item.amount
        return amount

    for x in income:
        for y in source_list:
            finalrep[y] = get_income_source_amount(y)

    return Response({'income_source_data': finalrep}, status=status.HTTP_200_OK)


# Plan 
# GET | POST
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def plan_view(request):
    # GET
    if request.method == 'GET':        
        plan = Plan.objects.all()
        serializer = PlanSerializer(plan, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = PlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET | PUT | DELETE
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def plan_view_pk(request,pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
        serializer = PlanSerializer(plan)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # DELETE
    if request.method == 'DELETE':
        plan.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# Consultation 
# GET | POST
@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def consult_view(request):
    # GET
    if request.method == 'GET':        
        consult = Consult.objects.all()
        serializer = ConsultationSerializer(consult, many=True)
        return Response(serializer.data)
    # POST
    elif request.method == 'POST':
        serializer = ConsultationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
