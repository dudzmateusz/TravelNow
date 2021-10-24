import folium
from .get_details_list_of_hotels import details_hotels
from .get_photos_of_hotel import photos
from .get_locations_of_hotels import location

def generate_map(city,inb,ob,adults):
    dId = location(city)
    print(dId)
    z = details_hotels(dId, inb, ob, adults)
    x = str()
    y = str()

    if z['result']!='ERROR':
        try:
            for i in z['data']['body']['searchResults']['results']:
                x = i['coordinate']['lat']
                y = i['coordinate']['lon']
        except KeyError:
            for i in z['data']['body']['pdpHeader']['hotelLocation']:
                x= i['coordinates']['latitude']
                y= i['coordinates']['longitude']

    map1 = folium.Map(
        location=[x, y],
        prefer_canvas=True,
        tiles='Mapbox Bright',
        zoom_start=12,
    )
    for i in z['data']['body']['searchResults']['results']:
        x = i['coordinate']['lat']
        y = i['coordinate']['lon']
        image = i['id']
        img = photos(image)
        if i['guestReviews']:
            for ima in img['hotelImages']:
                url = str(ima['baseUrl'])
                ima_r = url.replace("{size}", "z")
                try:
                 html = folium.Html(
                        '<b>{}</b></br><b>{}|| {}</b> '
                        '<img style="width:15px; height:15px;" src="polls/static/polls/images/star.png"/></br>'
                        '<b>{} zł PLN/per night</b></br><img style="width:70%; height:70%;" src="{}"/></br>'
                        '{},{},{} </br> <a href="#">Zobacz więcej...</a>'.format(

                                                                                 i['name'],
                                                                                 i['guestReviews']['badgeText'],
                                                                                 i['starRating'],
                                                                                 i['ratePlan']['price']['exactCurrent'],
                                                                                 #i['ratePlan']['price']['info'],
                                                                                 ima_r,
                                                                                 i['address']['streetAddress'],
                                                                                 i['address']['postalCode'],
                                                                                 i['address']['locality']),
                                                                                 script=True


                     )
                except KeyError:
                    continue
                popup = folium.Popup(html, max_width=2650)
                folium.Marker(location=[x, y]
                              , popup=popup,
                              icon=folium.Icon(color="green")).add_to(map1)

            map1.save("polls/templates/polls/list_of_hotels.html")

