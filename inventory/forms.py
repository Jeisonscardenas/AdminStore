from django import forms

from .models import *

class FormDistributor(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = '__all__'

class FormItem(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class FormInvoice(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class FormPoint(forms.ModelForm):
    class Meta:
        model = Point
        fields = '__all__'

class FormDetail(forms.ModelForm):
    class Meta:
        model = Detail_invoice
        fields = '__all__'