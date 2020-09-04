import json

from django.shortcuts import render

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
                    "detailsUrl": "./static/moscow_legends.json"
                }
            }
        )

    context = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, 'index.html', {'places_geojson': json.dumps(context)})
