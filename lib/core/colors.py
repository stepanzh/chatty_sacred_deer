import sys
from itertools import cycle

def color(code:int):
    return '\u001b[38;5;'+str(code)+'m'


class Colors:
    reset = '\u001b[0m'
    default = color(231)  # white

    boldwhite = '\u001b[37;1m'
    lowcontrastgrey = color(8)

    # light colors
    red = color(196)
    orange = color(214)
    yellow = color(11)
    green = color(10)
    lightblue = color(14)
    blue = color(21)
    purple = color(5)
    pink = color(13)

    boldgreen = '\u001b[32;1m'
    boldyellow = '\u001b[33;1m'
    boldblue = '\u001b[34;1m'

    rainbow_set = [red, orange, yellow, green, lightblue, blue, purple]

    @classmethod
    def rainbow(cls, s):
        """Rainbows string."""
        colors = cycle(cls.rainbow_set)
        new = next(colors)
        for i, c in enumerate(s):
            new += c
            if i != len(s) - 1 and c not in ' \n\b\r\t':
                new += next(colors)
        new += cls.reset
        return new

    @classmethod
    def colorise(cls, s:str, c:str):
        return c + str(s) + cls.reset

    @classmethod
    def palette(cls):
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(color(code) + code.ljust(4))
        print('\u001b[0m')

    @classmethod
    def colorized_print(cls, color):
        def wrap(f):
            def wrapped(*args, **kwargs):
                print(color, end='')
                r = f(*args, **kwargs)
                print(cls.reset, end='')
                return r
            return wrapped
        return wrap

if __name__ == "__main__":
    Colors.palette()
