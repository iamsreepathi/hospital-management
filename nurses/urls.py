from django.urls import path

from .views import NurseListView, NurseDetailView

# Blog application URLs

app_name = "nurses"

urlpatterns = [
    path("", NurseListView.as_view(), name="list"),
    path("<int:pk>/", NurseDetailView.as_view(), name="detail"),
]
