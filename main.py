"""Colors API, utilities for color lovers"""
import hug
from ccolors import random_rgb, rgb_to_hex
from ccolors import complimentary as ccomplimentary
@hug.get()

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

@hug.get(examples="r=100&g=200&b=55")
def to_hex(r: hug.types.in_range(0, 256), g: hug.types.in_range(0, 256), b: hug.types.in_range(0, 256)):
    return {"hex": rgb_to_hex(r, g, b)}


@hug.get(examples=("hex=DD00FF", "hex=000","hex=123456"))
def to_rgb(hex: hug.types.text):
    (r, g, b) = hex_to_rgb(hex)
    return {
        "rgb": {
            "r": r,
            "g": g,
            "b": b,
        }
    }


@hug.get(examples="r=100&g=200&b=55")
def complimentary(r: hug.types.in_range(0, 256), g: hug.types.in_range(0, 256), b: hug.types.in_range(0, 256)):
    (rc, gc, bc) = ccomplimentary((r, g, b))
    return {
        "rgb": {
            "r": rc,
            "g": gc,
            "b": bc,
        }
    }
