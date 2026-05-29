from shapely.geometry import Point, Polygon


# Define zones manually for now
# Later dataset will provide these

ZONES = {

    "ENTRY": Polygon([
        (0, 0),
        (250, 0),
        (250, 720),
        (0, 720)
    ]),

    "BILLING": Polygon([
        (900, 0),
        (1280, 0),
        (1280, 720),
        (900, 720)
    ])
}


def get_zone(x, y):

    point = Point(x, y)

    for zone_name, polygon in ZONES.items():

        if polygon.contains(point):
            return zone_name

    return None