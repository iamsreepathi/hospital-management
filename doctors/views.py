from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Doctor


# Create your views here.
class DoctorListView(ListView):
    model = Doctor
    template_name = "doctor/list.html"
    paginate_by = 10

    table_columns = [
        {"title": "First Name", "key": "first_name"},
        {"title": "Last Name", "key": "last_name"},
        {"title": "Specialization", "key": "specialization"},
        {"title": "Contact Number", "key": "contact_number"},
        {"title": "Action", "key": "action"},
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"columns": self.table_columns})
        return context


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = "doctor/detail.html"
