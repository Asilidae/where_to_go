import json

from django.shortcuts import render

from places.models import Place


def index(request):
    # places = Place.objects.all()
    # features = []
    # for one_place in places:
    #     features.append(
    #         {
    #             "type": "Feature",
    #             "geometry": {
    #                 "type": "Point",
    #                 "coordinates": [one_place.lng, one_place.lon]
    #             },
    #             "properties": {
    #                 "title": one_place.title,
    #                 "placeId": one_place.pk,
    #                 "description_short": one_place.description_short,
    #                 "description_long": one_place.description_long
    #             }
    #         }
    #     )
    #
    # context = {
    #     "type": "FeatureCollection",
    #     "features": features
    # }

    context = {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.62, 55.793676]
          },
          "properties": {
            "title": "«Легенды Москвы",
            "placeId": "moscow_legends",
            "detailsUrl": "./static/moscow_legends.json"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [37.64, 55.753676]
          },
          "properties": {
            "title": "Крыши24.рф",
            "placeId": "roofs24",
            "detailsUrl": "./static/roofs24.json"
          }
        }
      ]
    }

    return render(request, 'index.html', {'places_geojson': json.dumps(context)})
