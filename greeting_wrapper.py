from curses import wrapper


def greet(func):
    def wrap(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrap


@greet
def shout(text):
    return text.upper()


@greet
def whisper(text):
    return text.lower()


shout("Hello test")
whisper("Hello test")
