from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

def main(request): 
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, 'main_page.html', context)

def add(request): 
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
       
      
    form = ExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'add_expense.html', context)

    
def update(request, expense_id): 
    expense = get_object_or_404(Expense, id = expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance = expense)
        if form.is_valid():
            form.save()
            return redirect('main')
    form = ExpenseForm(instance=expense)
    context = {
        'form': form
    }
    
    return render(request, 'update_expense.html', context)
    

def delete(request, expense_id): 
    expense = get_object_or_404(Expense, id = expense_id)
    expense.delete()
    return redirect('main')
