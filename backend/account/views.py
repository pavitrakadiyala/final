from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer, UserSerializer
# (myprojectenv) [root@pga cars]# cat views.py 

from django.shortcuts import render

# from cars.models import Car, Driver
from django.http import HttpResponse

def index(request):
    return render(request,'src\index.js')
    #return HttpResponse("<h1>Welcome to the System</h1>")

def car_detail(request, pk):

    owner_obj = Account.objects.get(pk=pk)


    context = {

        # "vehicles": car_objs,

        "drivers": owner_obj,

    }

    return render(request, "", context)

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]