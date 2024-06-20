from django.shortcuts import render
from .models import Payment
from datetime import datetime

def payment_list(request):
    month = request.GET.get('month')
    year = request.GET.get('year')
    
    if month and year:
        payments = Payment.objects.filter(payment_date__year=year, payment_date__month=month)
    else:
        payments = Payment.objects.all()

    current_year = datetime.now().year
    years = range(2020, current_year + 1)
    months = range(1, 13)

    return render(request, 'core/payment_list.html', {
        'payments': payments,
        'current_year': current_year,
        'years': years,
        'months': months
    })
