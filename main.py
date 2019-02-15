"""Colors API, utilities for color lovers"""
import hug
import ccolors
@hug.get()
def random():
    """Returns a random color."""
    (r,g,b) = ccolors.random_rgb()
    return {
        "hex": f"#{r:02x}{g:02x}{b:02x}",
        "rgb": {
            "r": r,
            "g": g,
            "b": b,
        }
        }
