from geopy import Nominatim
from geopy import distance as geopy_distance
from dataclasses import dataclass
import folium


@dataclass(frozen=True)
class StreetLocation:
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


@dataclass(frozen=True)
class GeoLocator:
    geolocator = Nominatim(user_agent="Geolocator")

    def street_location_from_adress(self, address) -> StreetLocation:
        geocode_location = self.geolocator.geocode(address)
        return StreetLocation(geocode_location.latitude, geocode_location.longitude)


def meter_distance(a1, a2):
    return int(geopy_distance.distance(a1.location, a2.location).meters)


def walk_time(a1, a2):
    meter_per_minute = 80
    distance = meter_distance(a1, a2)
    return int((distance / meter_per_minute))


def run():
    address = "Mireckiego 29, 42-200 Częstochowa"
    address2 = "Orkana 21, 42-200 Częstochowa"
    geo_locator = GeoLocator()
    address_location = geo_locator.street_location_from_adress(address)
    address2_location = geo_locator.street_location_from_adress(address2)
    meter_dist = meter_distance(address_location, address2_location)
    time = walk_time(address_location, address2_location)
    print(address_location.latitude, address_location.longitude)
    print(f"Dystans z {address} do {address2} wynosi: {meter_dist} m i zajmie: {time} min")
    map_address1 = [address_location.latitude, address_location.longitude]
    map_address2 = [address2_location.latitude, address2_location.longitude]
    m = folium.Map(location=[address_location.latitude, address_location.longitude], zoom_start=12)
    tooltip = "Click me!"
    folium.Marker(map_address1, popup=str(address), tooltip=tooltip).add_to(m)
    folium.Marker(map_address2, popup=str(address2), tooltip=tooltip).add_to(m)
    folium.PolyLine(
        [map_address1, map_address2],
        color="red",
        tooltip=tooltip,
        weight=3.5,
        opacity=0.5,
        popup=f"Dystans z {address} do {address2} wynosi: {meter_dist}m i zajmie: {time}min",
    ).add_to(m)
    m.save("map.html")


if __name__ == "__main__":
    run()
