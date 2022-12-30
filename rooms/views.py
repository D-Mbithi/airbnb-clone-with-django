from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from rooms import models

from .forms import SearchForm


class HomeListView(ListView):
    """Home ListView Defination."""

    model = models.Room
    template_name = "index.html"
    paginate_by: int = 10
    paginate_orphans: int = 5
    ordering = "created"


class RoomDetailView(DetailView):
    """Room detailview defination."""

    model = models.Room
    template_name = "rooms/room_detail.html"


class SearchView(View):
    """Search Class View"""

    def get(self, request):
        country = request.GET.get("country")

        if country:
            if request.method == "GET":
                form = SearchForm(request.GET)

                if form.is_valid():
                    city = form.cleaned_data.get("city")
                    country = form.cleaned_data.get("country")
                    room_type = form.cleaned_data.get("room_type")
                    price = form.cleaned_data.get("price")
                    guest = form.cleaned_data.get("guest")
                    baths = form.cleaned_data.get("baths")
                    price = form.cleaned_data.get("price")
                    beds = form.cleaned_data.get("beds")
                    instant = form.cleaned_data.get("instant")
                    superhost = form.cleaned_data.get("superhost")
                    amenities = form.cleaned_data.get("amenities")
                    facilities = form.cleaned_data.get("facilities")

                    filter_args = {}
                    filter_args["country"] = country

                    if city != "Anywhere":
                        filter_args["city__startswith"] = city

                    if guest:
                        filter_args["guest__gte"] = guest

                    if beds:
                        filter_args["beds__lte"] = beds

                    if price:
                        filter_args["price__lte"] = price

                    if baths:
                        filter_args["baths__lte"] = baths

                    if instant is True:
                        filter_args["instant_book"] = True

                    if superhost is True:
                        filter_args["host__super_host"] = True

                    if room_type:
                        filter_args["room_type"] = room_type

                    for amenity in amenities:
                        filter_args["amenities"] = amenity

                    for facility in facilities:
                        filter_args["facilities"] = facility

                    qs = models.Room.objects.filter(
                        **filter_args,
                    ).order_by("-created")

                    paginator = Paginator(qs, 10, orphans=5)
                    page = request.GET.get("page")

                    rooms = paginator.get_page(page)

                    context = {
                        "form": form,
                        "rooms": rooms,
                    }
        else:
            form = SearchForm()

            context = {
                "form": form,
            }
        template = "rooms/search.html"

        return render(request, template, context)
