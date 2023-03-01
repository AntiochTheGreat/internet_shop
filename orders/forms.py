from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    """This class describes form for order."""

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sherlok'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Holmes'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'England, London, Baker street, 221B',
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')
