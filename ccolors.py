from random import randint

def random_rgb():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return (r, g, b)


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"

def hex_to_rgb(hex):
    hex_len = len(hex)
    if hex_len == 6:
        r = int(hex[:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:], 16)
    elif hex_len == 3:
        r = int(hex[0]*2, 16)
        g = int(hex[1]*2, 16)
        b = int(hex[2]*2, 16)
    return (r, g, b)

def complimentary(color):
    r = 255 - color[0]
    g = 255 - color[1]
    b = 255 - color[2]
    return (r, g, b)