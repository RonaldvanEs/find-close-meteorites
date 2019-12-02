import requests
import math

def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(lz):
    return lz.get('distance', math.inf)
# 1.
landings = requests.get("https://data.nasa.gov/resource/gh4g-9sfh.json")
landings.status_code # should be 200
# 2.
meteor_data = landings.json()

# 3.
# My location Zoetermeer, 52.0691168264258 ,  4.494627242513502
my_loc = (52.0691168264258, 4.494627242513502)
for meteor in meteor_data:
    if not ('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_dist(float(meteor['reclat']),
                            float(meteor['reclong']),
                            my_loc[0],
                            my_loc[1])
meteor_data.sort(key=get_dist)
# Show the firts 10 items
print(meteor_data[0:10])
