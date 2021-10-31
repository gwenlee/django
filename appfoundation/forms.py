from django import forms
from django.core.exceptions import ValidationError

#Question: Do you know what and how 'lable', 'widget' are working in Django?
class NameForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=15)
    category = forms.ChoiceField(choices=[('questions','questions'),('other','other')])


def must_be_empty(input):
    #Comment: There is no "NULL" in Python, instead it is "None"
    #Comment: 'if val' is not the same as 'if val IS NOT None' 
    #Link: https://towardsdatascience.com/python-the-boolean-confusion-f7fc5288f0ce
    if input:
        raise ValidationError("Are you a human?")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
    sender_email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    force_field = forms.CharField(required=False,widget=forms.HiddenInput,
    label="If you are human, leave this empty", validators=[must_be_empty])


