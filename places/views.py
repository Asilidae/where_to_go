import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


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
                  {'places_geojson': json.dumps(context)})


def get_place_by_id(request, id):
    place = get_object_or_404(Place, pk=id)
    images = [one_image.image.url for one_image in place.image.all()]
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
