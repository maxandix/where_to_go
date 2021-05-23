from django.shortcuts import render
from places.models import Place
from django.urls import reverse


def index_page(request):
    places = Place.objects.all()
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
                "detailsUrl": reverse('place-place_details', kwargs={'place_id': place.id})
            }
        })
    places_geojson = {
        "type": "FeatureCollection",
        "features": features,
    }

    context = {
        "places_geojson": places_geojson,
    }
    return render(request, 'index.html', context)
