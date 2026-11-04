from django import forms
from electronica.models import Electronics


class ElectronicaForm(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = "__all__"