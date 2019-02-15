from random import randint

def random_rgb():
    r = randint(0, 256)
    g = randint(0, 256)
    b = randint(0, 256)
    return (r, g, b)