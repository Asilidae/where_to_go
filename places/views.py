import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from places.models import Place
import places.services as building_route

def index(request):
    places = Place.objects.all()
    features = []
    for one_place in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [one_place.lng, one_place.lon]
                },
                "properties": {
                    "title": one_place.title_short,
                    "placeId": one_place.place_id,
                    "detailsUrl": reverse('place', kwargs={'id': one_place.pk})
                }
            }
        )

    context = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request,
                  'index.html',
                  {'places_geojson': context})


def get_place_by_id(request, id):
    place = get_object_or_404(Place, pk=id)
    images = [one_image.image.url for one_image in place.images.all()]
    context = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lon,
            "lng": place.lng
        }
    }

    return JsonResponse(context,
                        safe=False,
                        json_dumps_params={'ensure_ascii': False, 'indent': 1})


@csrf_exempt
def save_selected_places(request):
    if request.method == 'POST':
        place_ids = json.loads(request.body)
        print(place_ids)  # Log the received data
        coordinates = list(Place.objects.filter(id__in=place_ids).values('place_id', 'lon', 'lng'))
        print(coordinates)
        # ... Process the data as needed ...
        min_route, min_distance = building_route.optimal_route(coordinates)
        print(min_route)
        print(min_distance)

        route = building_route.nearest_neighbour(coordinates)
        print(route)

        building_route.map_generated(route)

        return JsonResponse({"message": "Data received successfully."})
    else:
        return JsonResponse({"error": "Invalid request method."})
