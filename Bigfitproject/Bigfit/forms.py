from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label="Username", max_length=128)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput())



class RegisterForm(forms.Form):
    SEX_CHOICES = (
                 ('M', 'Male'), ('F', 'Female')
    )
    username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    target_weight = forms.IntegerField(label="Target Weight")
    feet= forms.IntegerField(label="Feet")
    inches= forms.IntegerField(label="Inches")
    date_of_birth = forms.DateField(label="Birth Date")
    zip_code = forms.CharField(label="zip code")
    gender = forms.ChoiceField(label='Sex',choices=SEX_CHOICES)


class WeightinputForm(forms.Form):
    current_weight = forms.IntegerField(label="Current Weight")
