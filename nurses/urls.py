from django.urls import path

from .views import NurseListView, NurseDetailView, NurseReviewView, NurseCreateView

# Blog application URLs

app_name = "nurses"

urlpatterns = [
    path("", NurseListView.as_view(), name="list"),
    path("add/", NurseCreateView.as_view(), name="add"),
    path("<int:pk>/", NurseDetailView.as_view(), name="detail"),
    path("<int:nurse_id>/rating", NurseReviewView.as_view(), name="rating"),
]
