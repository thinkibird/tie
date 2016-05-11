from django import forms

from .models import Work_with_us, Work_for_us


class WithUsForm(forms.ModelForm):

    class Meta:
        model = Work_with_us
        fields = ('Name', 'Email','PhoneNo','Address', 'Details')


class ForUsForm(forms.ModelForm):

    class Meta:
        model = Work_for_us
        fields = ('Name', 'Email','PhoneNo','Address', 'Details')