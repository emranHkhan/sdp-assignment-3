from django.shortcuts import render, redirect
from . import forms

def add(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('task.show')
    else:
        category_form = forms.CategoryForm()

    return render(request, 'add-category.html', {'form': category_form})        