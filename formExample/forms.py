from django import forms
# from django.core.validators import ValidationError

# def validateEmail(value):
#     if value.endswith('@mytectra.com') is False:
#         raise ValidationError('Email should end with @mytectra.com')
#
# def validateName(name):
#     if name.isdigit():
#         raise ValidationError('Invalid Name')
#     elif name.find(' ') > 0:
#         raise ValidationError('Spaces within characters is not allowed')

class FormExample(forms.Form):
    cityValues = (
        ('', '--Select option--'),
        ('Chennai', 'Chennai'),
        ('Bangalore', 'Bangalore'),
        ('Pune', 'Pune'),
        ('Mumbai', 'Mumbai')
    )
    city = forms.ChoiceField(choices=cityValues)

    gn = (
        ('f', 'female'),
        ('m', 'male')
    )
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)

    is_active = forms.CharField(widget=forms.CheckboxInput)
    is_not_active = forms.BooleanField()

    username = forms.CharField(
        # arguments to character fields / form options & validation
        label='Employee Name',
        min_length=8, max_length=14,
        required=True,
        error_messages={
            'required': 'Employee Name cannot be blank !',
            'min_length': 'Please enter atleast 8 characters !',
        },
        # initial='xyz$',
        # help_text='Please use special characters in Employee Name !',
        widget=forms.TextInput(attrs={
            'placeholder': 'Employee Name'
        }),
        # validators=[validateName],

    )
    email = forms.EmailField(
        # validators=[validateEmail],
        widget=forms.TextInput(attrs={
            'placeholder': 'kaustubh9031@gmail.com'
        })
    )
    address = forms.CharField(
        widget=forms.Textarea
        # widget=forms.NumberInput
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean(self):
        formValues = self.cleaned_data
        print(formValues)

        if 'username' in formValues:
            if formValues['username'].isdigit():
                self.errors['username'] = ['invalid username']

        if 'email' in formValues:
            if formValues['email'].endswith('@mytectra.com') is False:
                self.errors['email'] = ['email should end with @mytectra.com']

        if 'password' in formValues and 'confirm_password' in formValues:
            if formValues['password'] != formValues['confirm_password']:
                self.errors['confirm_password'] = ['password mismatch']

        return formValues