from django.urls import path
from .views import AccountListCreateView, TransactionListCreateView, UserCreateView

urlpatterns = [
    path('ok/', AccountListCreateView.as_view(), name='accounts-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transactions-list-create'),
    path('users/', UserCreateView.as_view(), name='user-create'),
    # Add other URL patterns here as needed
]