from django.urls import include, path

from rooms import views as room_views

app_name = "core"


urlpatterns = [
    path("", room_views.HomeListView.as_view(), name="home"),
]
