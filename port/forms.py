from django import forms
from port.models import Jongmok
from bootstrap_datepicker_plus import DatePickerInput
from datetime import date

app_name = 'port'

class BtestForm(forms.Form):
    stock = forms.ChoiceField(choices=[
    (item.code, item.name) for item in Jongmok.objects.all()])

    today = date.today()
    start_date =forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
        #, initial=today.replace(year=today.year-1, day=1)
        , initial=today.replace(year=today.year - 1)
    )

    end_date = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
        , initial=date.today
    )

