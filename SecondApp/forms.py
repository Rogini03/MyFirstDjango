from django import forms


class RegisterForm(forms.Form):
    stdname = forms.CharField(max_length=20)
    stdclass = forms.IntegerField()
    stdsection = forms.CharField(max_length=2)
    joindate = forms.DateField()



