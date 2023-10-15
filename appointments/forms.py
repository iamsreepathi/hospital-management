from django import forms
from .models import Appointment, GENDER


class DoctorAppointmentForm(forms.ModelForm):
    text_input_class = "border rounded p-2 w-full outline-none"
    full_name = forms.CharField(
        label="Patient Name",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "John Doe",
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
    gender = forms.ChoiceField(
        choices=GENDER,
        label="Gender",
        required=True,
        widget=forms.RadioSelect(
            attrs={"class": "text-emerald-600 font-semibold text-sm"}
        ),
    )
    appt_slot = forms.DateField(
        label="Appointment Time",
        required=True,
        input_formats=["%Y-%m-%d"],
        widget=forms.DateInput(
            attrs={"class": text_input_class, "type": "date"},
        ),
    )
    reason = forms.CharField(
        label="Reason",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": text_input_class,
                "placeholder": "Body checkup",
            }
        ),
    )
    notes = forms.CharField(
        label="Notes",
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": text_input_class,
                "placeholder": "Notes...",
                "rows": "3",
            }
        ),
    )

    class Meta:
        model = Appointment
        fields = (
            "full_name",
            "email",
            "contact_number",
            "address",
            "appt_slot",
            "reason",
            "notes",
            "gender",
        )
