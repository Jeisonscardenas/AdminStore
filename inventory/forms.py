from django import forms

from .models import *

class FormDistributor(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    nit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    phone= forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

class FormItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))  

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cc = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'})) 
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone=forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'})) 

class FormInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

    
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    cost = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    iva = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))


class FormPoint(forms.ModelForm):
    class Meta:
        model = Point
        fields = '__all__'

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    box_budget =  forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

class FormDetail(forms.ModelForm):
    class Meta:
        model = Detail_invoice
        fields = '__all__'

    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))