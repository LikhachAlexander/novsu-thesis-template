import numpy as np
from scipy.optimize import differential_evolution
from geopy.distance import distance as hav
import geopy
import math


def dist_error(ll, r_map):
    err = 0
    for s in r_map:
        err += np.square(hav(ll, (s[0], s[1])).m - s[2])
    return err


def get_bounds(x0, w=200, h=200):
    start = geopy.Point(x0)
    hypotenuse = math.hypot(w/1000, h/1000)
    northeast_angle = 0 - math.degrees(math.atan(w/h))
    southwest_angle = 180 - math.degrees(math.atan(w/h))
    d = hav(kilometers=hypotenuse/2)
    ne = d.destination(point=start, bearing=northeast_angle)
    sw = d.destination(point=start, bearing=southwest_angle)
    bounds = []
    bounds.append(sorted([ne.latitude, sw.latitude]))
    bounds.append(sorted([ne.longitude, sw.longitude]))
    return bounds


def localize(r_map):
    """r_map = [(lat_0, lon_0, r_0), ..., (lat_n, lon_n, r_n)]"""
    lat_s, lon_s = 0, 0
    for s in r_map:
        lat_s += s[0]
        lon_s += s[1]
    n = len(r_map)
    x0 = [lat_s / n, lon_s / n]
    dist_opt = lambda x: dist_error(x, r_map)
    bounds = get_bounds(x0)
    result = differential_evolution(dist_opt, bounds)
    return result.x
