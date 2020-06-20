from django import forms


class EntryForm(forms.Form):
    bedrooms = forms.CharField(required=True, widget=forms.NumberInput())
    bathrooms = forms.CharField(required=True, widget=forms.NumberInput())
    square_feet = forms.CharField(
        required=False,
        help_text="Not required",
        widget=forms.NumberInput()
    )
    address = forms.CharField(
        required=True,
        help_text="Street address",
        widget=forms.Textarea(attrs={'rows': '3'})
    )
    city = forms.CharField(
        required=True,
    )
    country = forms.CharField(
        required=True,
    )
    agency = forms.CharField(
        required=False,
        help_text="Not required"
    )
    price = forms.CharField(
        required=True,
        help_text="Price per month"
    )
    image = forms.FileField(
        required=True,
    )
