from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Doctor
from appointments.models import Appointment
from django.core.paginator import Paginator


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
    paginate_by = 10

    table_columns = [
        {"title": "Appt Date", "key": "date"},
        {"title": "Last Visited", "key": "last_visit"},
        {"title": "Patient", "key": "patient"},
        {"title": "Appt Status", "key": "status"},
        {"title": "Action", "key": "action"},
    ]

    def get_context_data(self, **kwargs):
        context = super(DoctorDetailView, self).get_context_data(**kwargs)
        appointments = self.get_appointments()
        context["appointments"] = appointments
        context["page_obj"] = appointments
        context.update({"columns": self.table_columns})
        return context

    def get_appointments(self):
        queryset = (
            Appointment.objects.select_related("patient")
            .filter(doctor=self.object)
            .only(
                "id",
                "date",
                "last_visit",
                "status",
                "patient__first_name",
                "patient__last_name",
            )
        )
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get("page")
        appointments = paginator.get_page(page)
        return appointments
