from django.urls import path

from .views import PatientListView, PatientDetailView, PatientCreateView

# Blog application URLs

app_name = "patients"

urlpatterns = [
    path("", PatientListView.as_view(), name="list"),
    path("add/", PatientCreateView.as_view(), name="add"),
    path("<int:pk>/", PatientDetailView.as_view(), name="detail"),
]
