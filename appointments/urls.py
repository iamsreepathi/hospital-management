from django.urls import path

from .views import AppointmentListView, AppointmentDetailView, DoctorAppointmentView

# Blog application URLs

app_name = "appointments"

urlpatterns = [
    path("", AppointmentListView.as_view(), name="list"),
    path("<int:pk>/", AppointmentDetailView.as_view(), name="detail"),
    path("doctor/<int:doctor_id>", DoctorAppointmentView.as_view(), name="doctor"),
]
