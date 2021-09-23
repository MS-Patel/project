from bank.models import Landing
from django import forms


class LandingForm(forms.Form):

    full_name = forms.CharField(
        label='Full Name', max_length=100,)
    phone = forms.RegexField(label='Phone no',
                             regex=r'^\+?1?\d{9,15}$', error_messages={'Error': "Enter Valid phone number"})
    email = forms.EmailField(label='Email Id', max_length=150,)
    credit = forms.FloatField(label='Credit amount')
    debit = forms.FloatField(label='Withdraw amount')

    class Meta:
        model = Landing
        fields = ('username', 'full_name' 'email', 'phone', 'balance')
