from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Appointment


# Create your views here.
class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment/list.html"
    paginate_by = 10

    table_columns = [
        {"title": "Appt Date", "key": "date"},
        {"title": "Patient", "key": "patient"},
        {"title": "Doctor", "key": "doctor"},
        {"title": "Appt Status", "key": "status"},
        {"title": "Action", "key": "action"},
    ]

    def get_queryset(self):
        queryset = Appointment.objects.select_related("patient", "doctor").only(
            "id",
            "date",
            "last_visit",
            "status",
            "patient__first_name",
            "patient__last_name",
            "doctor__first_name",
            "doctor__last_name",
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"columns": self.table_columns})
        return context


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = "appointment/detail.html"
