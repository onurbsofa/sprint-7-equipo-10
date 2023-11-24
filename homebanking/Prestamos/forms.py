from django import forms
from .models import Prestamo

class SolicitudPrestamoForm(forms.ModelForm):
    DAY_CHOICES = [(str(i), str(i)) for i in range(1, 32)]
    MONTH_CHOICES = [(str(i), str(i)) for i in range(1, 13)]
    YEAR_CHOICES = [(str(i), str(i)) for i in range(2020, 2030)]

    loan_day = forms.ChoiceField(label='Día', choices=DAY_CHOICES)
    loan_month = forms.ChoiceField(label='Mes', choices=MONTH_CHOICES)
    loan_year = forms.ChoiceField(label='Año', choices=YEAR_CHOICES)
    loan_date_label = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_date', 'loan_total']
       

    