# Colors API


Utilities for Color lovers. Provides basic utitilities for working with rgb
colors and named colors.

This project could be used in 3 ways:

1. As a library for your project.
2. As a command line utility
3. As a Rest API at https://colors.hectorip.com


- *random* -> Random Color in rgb
- *complimentary* -> Receives a color and returns the complimentary
- *color_scheme* -> Returns a color scheme

## About

Developed in Python for fun, with [Hug](https://python-hug.com) and [TDD](https://tdd.com).

## Local install

1. Clone this repo and move to the generated folder.
2. (Optional but recommended) Create and activate a [virtualenv](https://docs.python-guide.org/dev/virtualenvs/).
3. Install the requirments  with `pip install -r requirements.txt`
4. (Optional) Run the tests. The test suite was written using *unittest*. Simply run:
```bash
python -m tests.ccolors_test
```
5. Init *hug*:
```
hug -f main.py
```