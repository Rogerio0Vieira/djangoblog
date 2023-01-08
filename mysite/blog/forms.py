from django import forms 

class EmailPostForm(forms.Form):
  name = forms.CharField(max_length=25)
  email = forms.EmailField()
  to = forms.EmailField()
  comments = forms.ChoiceField(required=False, widget=forms.Textarea)