"""Colors API, utilities for color lovers"""
import hug
import ccolors
@hug.get()
def random():
    """Returns a random color."""
    (r,g,b) = ccolors.random_rgb()
    return {
        "hex": "This is a random color",
        "rgb": {
            "r": r,
            "g": g,
            "b": b,
        }
        }
