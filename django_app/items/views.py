from django.shortcuts import render, redirect
from .models import Item
from django import forms

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']

def item_list(request):
    items = Item.objects.all()
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('items')
    return render(request, 'items/item_list.html', {'items': items, 'form': form})
