from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Patient
from django.urls import reverse
from .forms import CreatePatientForm


# Create your views here.
class PatientListView(ListView):
    model = Patient
    template_name = "patient/list.html"
    paginate_by = 10

    table_columns = [
        {"title": "First Name", "key": "first_name"},
        {"title": "Last Name", "key": "last_name"},
        {"title": "Gender", "key": "gender"},
        {"title": "DOB", "key": "dob"},
        {"title": "Contact Number", "key": "contact_number"},
        {"title": "Action", "key": "action"},
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"columns": self.table_columns})
        return context


class PatientDetailView(DetailView):
    model = Patient
    template_name = "patient/detail.html"


class PatientCreateView(CreateView):
    template_name = "patient/create.html"
    form_class = CreatePatientForm
    model = Patient

    def get_success_url(self) -> str:
        return reverse("patients:list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
