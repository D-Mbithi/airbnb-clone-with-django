from django.urls import path

from rooms import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>/", views.RoomDetailView.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
