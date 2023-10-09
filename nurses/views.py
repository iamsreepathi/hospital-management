from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Nurse


# Create your views here.
class NurseListView(ListView):
    model = Nurse
    template_name = "nurse/list.html"
    paginate_by = 10

    table_columns = [
        {"title": "First Name", "key": "first_name"},
        {"title": "Last Name", "key": "last_name"},
        {"title": "Email", "key": "email"},
        {"title": "Contact Number", "key": "contact_number"},
        {"title": "Action", "key": "action"},
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"columns": self.table_columns})
        return context


class NurseDetailView(DetailView):
    model = Nurse
    template_name = "nurse/detail.html"
