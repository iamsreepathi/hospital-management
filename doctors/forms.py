from django import forms
from .models import Doctor, GENDER


class CreateDoctorForm(forms.ModelForm):
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
    specialization = forms.CharField(
        label="Specialization",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "Neurology",
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
    about = forms.CharField(
        label="About",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": text_input_class,
                "placeholder": "Tell me something about you....",
                "rows": "3",
            }
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
        model = Doctor
        fields = (
            "first_name",
            "last_name",
            "specialization",
            "email",
            "contact_number",
            "address",
            "about",
            "gender",
        )
