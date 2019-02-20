"""Esto es una prueba de hug"""
import hug


@hug.get(versions=1)
@hug.local()
def hello_hug():
    return "hello hug"


@hug.get(versions=2, examples="name=Hector")
@hug.local()
@hug.cli()
def hello_hug(name : hug.types.length(2, 50)):
    return {
        "message": f"hello {name}"
    }

if __name__ == "__main__":
    hello_hug.interface.cli()

