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
                                       #, max_value="2000", min_value="0")
    feet= forms.IntegerField(label="Feet")
                             #, max_value="10", min_value="0")
    inches= forms.IntegerField(label="Inches")
                               #, max_value="12", min_value="0")
    date_of_birth = forms.DateField(label="Birth Date")
    zip_code = forms.CharField(label="zip code", max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="phone", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label="email", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gender = forms.ChoiceField(label='Sex', choices=SEX_CHOICES)


class WeightinputForm(forms.Form):
    current_weight = forms.IntegerField(label="Current Weight")


class CalorieinputForm(forms.Form):
    current_calorie = forms.IntegerField(label="Current Calorie")
