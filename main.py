"""Colors API, utilities for color lovers"""
import hug
from ccolors import random_rgb, rgb_to_hex
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
def to_hex(r:int, g:int, b:int):
    return {"hex": rgb_to_hex(r, g, b)}