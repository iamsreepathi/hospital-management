from django import forms
from .models import Patient, GENDER


class CreatePatientForm(forms.ModelForm):
    text_input_class = "border rounded p-2 w-full outline-none"
    first_name = forms.CharField(
        label="First Name",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "John",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "Doe",
            }
        ),
    )
    email = forms.EmailField(
        label="Email Address",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "johndoe@example.com",
            }
        ),
    )
    contact_number = forms.CharField(
        label="Phone Number",
        required=True,
        max_length=15,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "(605) 123 4567",
            }
        ),
    )
    address = forms.CharField(
        label="Address",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "123 New Line Dr, Sioux Falls, SD, 57108",
            }
        ),
    )
    dob = forms.DateField(
        label="DOB",
        required=True,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={"class": text_input_class, "type": "date"},
        ),
    )
    gender = forms.ChoiceField(
        choices=GENDER,
        label="Gender",
        required=True,
        widget=forms.RadioSelect(
            attrs={"class": "text-emerald-600 font-semibold text-sm"}
        ),
    )

    class Meta:
        model = Patient
        fields = (
            "first_name",
            "last_name",
            "dob",
            "email",
            "contact_number",
            "address",
            "gender",
        )
