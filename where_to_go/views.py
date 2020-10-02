from django.shortcuts import render
from places.models import Place


def index_page(request):
    places = Place.objects.all()

    data = {
        "type": "FeatureCollection",
        "features": [],
    }

    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": "./static/places/moscow_legends.json"
            }
        })

    data["features"] = features

    # data = {
    #     "type": "FeatureCollection",
    #     "features": [
    #         {
    #             "type": "Feature",
    #             "geometry": {
    #                 "type": "Point",
    #                 "coordinates": [37.62, 55.793676]
    #             },
    #             "properties": {
    #                 "title": "«Легенды Москвы",
    #                 "placeId": "moscow_legends",
    #                 "detailsUrl": "./static/places/moscow_legends.json"
    #             }
    #         },
    #         {
    #             "type": "Feature",
    #             "geometry": {
    #                 "type": "Point",
    #                 "coordinates": [37.64, 55.753676]
    #             },
    #             "properties": {
    #                 "title": "Крыши24.рф",
    #                 "placeId": "roofs24",
    #                 "detailsUrl": "./static/places/roofs24.json"
    #             }
    #         }
    #     ]
    # }

    context = {
        "data": data,
    }
    return render(request, 'index.html', context)
