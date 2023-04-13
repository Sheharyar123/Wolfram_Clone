from django import forms
from django_countries.fields import CountryField


class ContactForm(forms.Form):
    CHOICES = (
        ("Business/Government", "Business/Government"),
        ("Academic/Faculty", "Academic/Faculty"),
        ("Student", "Student"),
        ("Nonprofessional/Hobbyist", "Nonprofessional/Hobbyist"),
    )
    message = forms.CharField(widget=forms.Textarea)
    choices = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}), choices=CHOICES
    )
    organization = forms.CharField(max_length=255, widget=forms.TextInput)
    department = forms.CharField(max_length=255, widget=forms.TextInput)
    first_name = forms.CharField(max_length=255, widget=forms.TextInput)
    last_name = forms.CharField(max_length=255, widget=forms.TextInput)
    email = forms.CharField(max_length=255, widget=forms.TextInput)
    phone_no = forms.CharField(max_length=50, widget=forms.TextInput)
    extension = forms.CharField(max_length=255, widget=forms.TextInput)
    country = CountryField(blank_label="(Select country)").formfield()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != "choices":
                self.fields[field].widget.attrs.update({"class": "form-control"})
