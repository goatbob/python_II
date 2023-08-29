
def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


@do_twice
def print_func():
    print("This confuses me.")


if __name__ == "__main__":
    print_func()

