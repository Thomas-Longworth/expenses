from django.shortcuts import render, redirect
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

    
def update(request): 
    return render(request, 'update_expense.html')
    

def delete(request): 
    return render(request, 'delete_expense.html')
