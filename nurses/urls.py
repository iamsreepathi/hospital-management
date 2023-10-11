from django.urls import path

from .views import NurseListView, NurseDetailView, NurseReviewView

# Blog application URLs

app_name = "nurses"

urlpatterns = [
    path("", NurseListView.as_view(), name="list"),
    path("<int:pk>/", NurseDetailView.as_view(), name="detail"),
    path("<int:nurse_id>/rating", NurseReviewView.as_view(), name="rating"),
]
