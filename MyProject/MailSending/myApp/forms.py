from django import forms


class ContactUs(forms.Form):
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	body = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}))