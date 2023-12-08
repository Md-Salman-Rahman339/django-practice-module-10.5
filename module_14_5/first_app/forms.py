from django import forms
from django.forms.widgets import NumberInput
import datetime



class StudentData(forms.Form):
    name = forms.CharField()
    # email =forms.CharField(widget=forms.EmailInput)
    comment=forms.CharField(widget=forms.Textarea)
    email=forms.EmailField()
    # agree=forms.BooleanField()
    date=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birthday=date=forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    BIRTH_YEAR_CHOICES = ['2001', '2002', '2003']
    birth_year=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    email_address=forms.EmailField(label="please enter your email Address",required=False)
    message=forms.CharField(max_length=10,)
    first_name=forms.CharField(initial='Your Name')
    agree=forms.BooleanField(initial=True)
    day=forms.DateField(initial=datetime.date.today)
    
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color=forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
    multi_choice=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'datetime-local'}))
   