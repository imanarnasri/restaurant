from django import forms
from page.models import Reservation

class Reservation_create_form(forms.ModelForm):
    class Meta:
        model = Reservation

        fields = ('name','phone','no_of_people','date','time')