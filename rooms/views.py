from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django_countries import Countries

from .models import Amenity, Facility, Room, RoomType


class HomeListView(ListView):
    """
    Home ListView Defination.
    """

    model = Room
    template_name = "index.html"
    paginate_by: int = 10
    paginate_orphans = 5
    ordering = "created"


class RoomDetailView(DetailView):
    """
    Room detailview defination.
    """

    model = Room
    template_name = "rooms/room_detail.html"


def search(request):
    city = str.capitalize(request.GET.get("city", "anywhere"))
    countries = Countries()
    s_room_type = int(request.GET.get("roomtype", 0))
    s_country = request.GET.get("country")
    s_amenity = request.GET.getlist("amenity")
    s_facility = request.GET.getlist("facility")
    s_superhost = bool(request.GET.get("super_host", False))
    s_instant = bool(request.GET.get("instant", False))
    price = int(request.GET.get("price", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    bath = int(request.GET.get("bath", 0))
    guest = int(request.GET.get("quest", 0))
    room_types = RoomType.objects.all()
    amenities = Amenity.objects.all()
    facilities = Facility.objects.all()
    template = "rooms/search.html"

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = s_country

    if guest != 0:
        filter_args["guest__gte"] = guest

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__lte"] = beds

    if price != 0:
        filter_args["price__lte"] = price

    if s_instant is True:
        filter_args["instant_book"] = True

    if s_superhost is True:
        filter_args["host__super_host"] = True

    if s_room_type != 0:
        filter_args["room_type__pk"] = s_room_type

    if len(s_amenity) > 0:
        for amenity in s_amenity:
            filter_args["amenities__pk"] = int(amenity)

    if len(s_facility) > 0:
        for facility in s_facility:
            filter_args["facilities__pk"] = int(facility)

    rooms = Room.objects.filter(**filter_args)

    context = {
        "city": city,
        "s_country": s_country,
        "countries": countries,
        "s_room_type": s_room_type,
        "s_amenity": s_amenity,
        "s_facility": s_facility,
        "s_superhost": s_superhost,
        "s_instant": s_instant,
        "room_types": room_types,
        "price": int(price),
        "bedrooms": int(bedrooms),
        "beds": int(beds),
        "bath": int(bath),
        "guest": int(guest),
        "amenities": amenities,
        "facilities": facilities,
        "rooms": rooms,
    }
    return render(request, template, context)
