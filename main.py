"""Colors API, utilities for color lovers"""
import hug
from hug.middleware import CORSMiddleware
from ccolors import random_rgb, rgb_to_hex, hex_to_rgb, generate_scheme
from ccolors import complementary as ccomplementary  # Didn't remember imports could be aliased

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.get(versions=1)
@hug.local()
def random():
    """Returns a random color."""
    (r,g,b) = random_rgb()
    return {
        "hex": rgb_to_hex(r, g, b),
        "rgb": {
            "r": r,
            "g": g,
            "b": b,
        }
    }

@hug.get(examples="r=100&g=200&b=55", versions=1)
@hug.local()
def to_hex(r: hug.types.in_range(0, 256), g: hug.types.in_range(0, 256), b: hug.types.in_range(0, 256)):
    return {"hex": rgb_to_hex(r, g, b)}


@hug.get(examples=("hex=DD00FF", "hex=000","hex=123456"), versions=1)
@hug.local()
def to_rgb(hex: hug.types.text):
    (r, g, b) = hex_to_rgb(hex)
    return {
        "rgb": {
            "r": r,
            "g": g,
            "b": b,
        }
    }


@hug.get('/rgb/complementary', examples=("r=100&g=200&b=55"), versions=1)
@hug.local()
def complementary_rgb(r: hug.types.in_range(0, 256), g: hug.types.in_range(0, 256), b: hug.types.in_range(0, 256)):
    (rc, gc, bc) = ccomplementary((r, g, b))
    return {
        "rgb": {
            "r": rc,
            "g": gc,
            "b": bc,
        }
    }


# TODO: This function overwrites the previous implementation
@hug.get('/hex/complementary', examples=("hex=FF0000", "hex=000"), versions=1)
@hug.local()
def complementary_hex(hex: hug.types.text):
    rgb = hex_to_rgb(hex)
    (r, g, b) = ccomplementary(rgb)
    hex_c = rgb_to_hex(r, g, b)
    return {
        "hex": hex_c
    }


@hug.get('/scheme', examples=("hex=FF0000", "hex=000"), versions=2)
@hug.local()
def scheme(hex: hug.types.text):
    return generate_scheme(hex)
