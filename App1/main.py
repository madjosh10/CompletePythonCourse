# Methods and functions
latitude = float("40.09")
longitude = float("-3.47")

antipode_latitude = latitude.__mul__(int("-1"))
anitpode_longitude = longitude.__add__(float("180"))

print(antipode_latitude)
print(anitpode_longitude)
