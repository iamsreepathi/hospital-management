from django.views.generic import ListView, DetailView, CreateView
from .models import Doctor, DoctorReview
from appointments.models import Appointment
from django.core.paginator import Paginator
from django.db.models import Avg, Count
from django.urls import reverse
from .forms import CreateDoctorForm


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
        {"title": "Patient Name", "key": "full_name"},
        {"title": "Appt Slot", "key": "appt_slot"},
        {"title": "Appt Status", "key": "status"},
        {"title": "Email Address", "key": "email"},
        {"title": "Action", "key": "action"},
    ]

    def get_context_data(self, **kwargs):
        context = super(DoctorDetailView, self).get_context_data(**kwargs)
        appointments = self.get_appointments()
        rat_avg = self.get_rating().get("avg")
        rating, rated, unrated = None, None, None
        if rat_avg:
            rating = round(rat_avg, 2)
            rated = round(rating)
            unrated = 5 - rated
        context.update(
            {
                "appointments": appointments,
                "page_obj": appointments,
                "rating": rating,
                "rated": rated,
                "unrated": unrated,
                "columns": self.table_columns,
            }
        )
        return context

    def get_rating(self):
        return self.object.doctorreview_set.aggregate(avg=Avg("rating"))

    def get_appointments(self):
        queryset = Appointment.objects.filter(doctor=self.object).only(
            "id",
            "full_name",
            "appt_slot",
            "email",
            "status",
        )
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get("page")
        appointments = paginator.get_page(page)
        return appointments


class DoctorReviewView(ListView):
    model = DoctorReview
    template_name = "review/list.html"
    paginate_by = 5

    def get_queryset(self):
        return (
            DoctorReview.objects.select_related("patient")
            .filter(doctor_id=self.kwargs["doctor_id"])
            .only(
                "id",
                "rating",
                "text",
                "date",
                "patient__first_name",
                "patient__last_name",
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ratings = self.get_overall_rating()
        context.update(ratings)
        return context

    def get_overall_rating(self):
        ratings = list()
        reviews = (
            DoctorReview.objects.filter(doctor_id=self.kwargs["doctor_id"])
            .values("rating")
            .annotate(total=Count("rating"))
            .all()
        )
        total_ratings = sum([r.get("total") for r in reviews])
        rating = (
            total_ratings
            if total_ratings == 0
            else round(
                sum([r.get("total") * r.get("rating") for r in reviews])
                / total_ratings,
                2,
            )
        )
        rated = round(rating)
        unrated = 5 - rated
        for i in range(5, 0, -1):
            review = next((r for r in reviews if r.get("rating") == i), False)
            if not review:
                ratings.append({"rating": i, "total": 0, "percentage": 0})
            else:
                total = review.get("total")
                percentage = round((total / total_ratings) * 100)
                ratings.append(
                    {
                        "rating": review.get("rating"),
                        "total": total,
                        "percentage": percentage,
                    }
                )
        return {
            "ratings": ratings,
            "total_ratings": total_ratings,
            "rating": rating,
            "rated": rated,
            "unrated": unrated,
        }


class DoctorCreateView(CreateView):
    template_name = "doctor/create.html"
    form_class = CreateDoctorForm
    model = Doctor

    def get_success_url(self) -> str:
        return reverse("doctors:list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
