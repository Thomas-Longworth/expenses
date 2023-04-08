from django.shortcuts import render, redirect
from .models import Expense

# Create your views here.


def main(request): 
    expenses = Expense.objects.all()
    context = {
        'Expenses': expenses
    }
    return render(request, 'main_page.html', context)

def add(request): 
    if request.method == "POST":
        name = request.POST.get('expense_name')
        Expense.objects.create(name=name)
        return redirect('main')
    return render(request, 'add_expense.html')


def update(request): 
    return render(request, 'update_expense.html')
    

def delete(request): 
    return render(request, 'delete_expense.html')
