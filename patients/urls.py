from django.urls import path

from .views import PatientListView, PatientDetailView

# Blog application URLs

app_name = "patients"

urlpatterns = [
    path("", PatientListView.as_view(), name="list"),
    path("<int:pk>/", PatientDetailView.as_view(), name="detail"),
]
