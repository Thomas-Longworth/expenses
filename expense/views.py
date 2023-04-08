from django.shortcuts import render

# Create your views here.



def main(request): 
    return render(request, 'main_page.html')


def add(request): 
    return render(request, 'add_expense.html')


def update(request): 
    return render(request, 'update_expense.html')
    

def delete(request): 
    return render(request, 'delete_expense.html')
