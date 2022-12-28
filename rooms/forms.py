from django import forms
from django_countries.fields import CountryField

from rooms import models


class SearchForm(forms.Form):
    """Search form defination."""

    qs_room_type = models.RoomType.objects.all()
    qs_amenities = models.Amenity.objects.all()
    qs_facilities = models.Facility.objects.all()

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KE").formfield()
    room_type = forms.ModelChoiceField(
        qs_room_type,
        required=False,
        empty_label="Any kind",
    )
    price = forms.IntegerField(required=False)
    guest = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    price = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    instant = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=qs_amenities,
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=qs_facilities,
        widget=forms.CheckboxSelectMultiple,
    )
