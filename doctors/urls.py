from django.urls import path

from .views import DoctorListView, DoctorDetailView, DoctorReviewView

# Blog application URLs

app_name = "doctors"

urlpatterns = [
    path("", DoctorListView.as_view(), name="list"),
    path("<int:pk>/", DoctorDetailView.as_view(), name="detail"),
    path("<int:doctor_id>/rating", DoctorReviewView.as_view(), name="rating"),
]
