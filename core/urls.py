from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('unpaid/', views.tenants_unpaid, name='tenants_unpaid'),
]
