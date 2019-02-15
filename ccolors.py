from random import randint

def random_rgb():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return (r, g, b)


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

