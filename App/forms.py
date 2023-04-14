from django import forms
from . models import Civilservants, Retirement, Reports

class CivilservantsForm(forms.ModelForm):
    class Meta:
        model = Civilservants
        fields = '__all__'
        # exclude = ("tested_at", "predictions")
class RetirementForm(forms.ModelForm):
    class Meta:
        model = Retirement
        fields = '__all__'
        # exclude = ("tested_at", "predictions")