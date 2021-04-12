from folium import Map


latitude = float("40.09")
longitude = float ("3.47")

# .__mul__() to multiply
# .__mul__(object())

antipode_lat = latitude.__mul__(int("-1"))

if longitude.__lt__(float("0")):
    antipode_longitude = longitude.__add__(float("180"))
elif longitude.__eq__(float("0")):
    antipode_longitude = float("180")
elif longitude.__gt__(float("180")):
    antipode_longitude = str("Invalid Longitude")
else:
    antipode_longitude = longitude.__sub__(float("180"))

print(antipode_lat)
print(antipode_longitude)