from django.views.generic import ListView, DetailView, CreateView
from .models import Appointment
from .forms import DoctorAppointmentForm
from django.urls import reverse
from django.db.utils import IntegrityError
from django.http import Http404


# Create your views here.
class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment/list.html"
    paginate_by = 10

    table_columns = [
        {"title": "Full Name", "key": "full_name"},
        {"title": "Appt Slot", "key": "appt_slot"},
        {"title": "Doctor", "key": "doctor"},
        {"title": "Appt Status", "key": "status"},
        {"title": "Action", "key": "action"},
    ]

    def get_queryset(self):
        queryset = Appointment.objects.select_related("doctor").only(
            "id",
            "full_name",
            "appt_slot",
            "status",
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


class DoctorAppointmentView(CreateView):
    template_name = "appointment/doctor.html"
    form_class = DoctorAppointmentForm
    model = Appointment

    def get_success_url(self):
        return reverse("appointments:list")

    def form_valid(self, form):
        appt = form.save(commit=False)
        appt.doctor_id = self.kwargs.get("doctor_id")
        try:
            appt.save()
        except IntegrityError:
            raise Http404("Doctor not found.")
        return super().form_valid(form)
