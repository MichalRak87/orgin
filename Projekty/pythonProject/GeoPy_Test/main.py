from geopy import Nominatim
from geopy import distance as geopy_distance
from dataclasses import dataclass


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
    address2 = "Kisielewskiego 27, 42-200 Częstochowa"
    geo_locator = GeoLocator()
    address_location = geo_locator.street_location_from_adress(address)
    address2_location = geo_locator.street_location_from_adress(address2)
    meter_dist = meter_distance(address_location, address2_location)
    time = walk_time(address_location, address2_location)
    print(f"Dystans z {address} do {address2} wynosi: {meter_dist} m i zajmie: {time} min")


if __name__ == "__main__":
    run()
