from django import forms
from .models import category, item
class postForm(forms.ModelForm):

    class Meta:
        model = item
        fields=('title', 'price', 'description','image')

class rangeform(forms.Form):
    pricefrom = forms.IntegerField()
    priceto = forms.IntegerField()
    def as_url_args(self):
        return urllib.urlencode(self.cleaned_data)
    #title = forms.CharField(label="title", max_length=100)
    #price = forms.IntegerField()
    #description = forms.CharField(widget=forms.Textarea)