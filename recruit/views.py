from django.shortcuts import render

def products_all(request):
    return render(request, 'index.html')

def products_by_category_all(request):
    return render(request, 'categories.html')