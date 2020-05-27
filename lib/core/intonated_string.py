import time, sys
from itertools import cycle


class ANSIEmphasisedString:
    """Works with strings including ANSI sequences."""
    _ansi_start = '\u001b'
    _ansi_end = 'm'

    @classmethod
    def parse_ansi(cls, s:str):
        """Returns sequence of ansi codes and pure strings.
        If s does not include ansi codes, returns s
        """
        parsed = []
        p = ''
        found_ansi = False
        i = 0
        while i < len(s):
            c = s[i]
            if c == cls._ansi_start:
                if p:
                    parsed.append(p)
                    p = ''
                while c != cls._ansi_end and i < len(s):
                    c = s[i]
                    p += c
                    i += 1
                parsed.append(p)
                p = ''
            else:
                while i < len(s):
                    if s[i] != cls._ansi_start:
                        p += s[i]
                        i += 1
                    else:
                        break
                parsed.append(p)
                p = ''
        return s if len(parsed) < 2 else tuple(parsed)

    @classmethod
    def is_ansi(cls, s:str):
        """Checks whether s is ansi sequence."""
        return s.startswith(cls._ansi_start) and s.endswith(cls._ansi_end)


class IntonatedString(ANSIEmphasisedString):
    char_pause = 0.02
    word_pause = 0.8

    def __init__(self, *args, word_pause:float=None, char_pause:float=None, end_pause:bool=False):
        """Constructs IntonationString.
        args must be 
          1) sequence of strings
          2) sequence of strings and numbers: s_1 n_1 s_2 n_2...
        s_i a string, that can contain ANSI escape codes.
        n_i defines pause in seconds.

        word_pause - defines default pause between parts (if n_i is ommited)
        char_pause - defines global pause between char printing
        end_pause - additional pause at the end
        """
        self.word_pause = word_pause if word_pause is not None else type(self).word_pause
        self.char_pause = char_pause if char_pause is not None else type(self).char_pause
        end_pause = self.word_pause if end_pause else None
        self.string = type(self).encode_from_iterable(args, self.word_pause, end_pause)

    def __repr__(self):
        return type(self).__name__ + '{}'.format(repr(self.string))

    def __str__(self):
        self.print()
        return ''

    def __len__(self):
        l = 0
        for part in self.string:
            if isinstance(part, tuple):  # search for pure string
                for pp in part:
                    if self.is_pure_str(pp):
                        l += len(pp)
            else:
                if self.is_pure_str(part):
                    l += len(part)
        return l

    def unzip(self):
        z = []
        for part in self.string:
            if isinstance(part, tuple):
                for pp in part:
                    z.append(pp)
            else:
                z.append(part)
        return z

    @classmethod
    def is_pause(cls, x):
        return isinstance(x, int) or isinstance(x, float) and x > 0

    @classmethod
    def is_pure_str(cls, s:str):
        return not cls.is_pause(s) and not cls.is_ansi(s)

    @classmethod
    def write_flush(cls, *args):
        w = 0
        for a in args:
            w += sys.stdout.write(a)
        sys.stdout.flush()
        return w

    def _pause(self, t:float=None):
        # t = t if t is not None else self.word_pause
        time.sleep(t)

    @classmethod
    def encode_from_iterable(cls, iterable, word_pause=None, end_pause=None):
        encoded = []
        for item in iterable:
            if cls.is_pause(item):
                encoded.append(float(item))
            elif isinstance(item, str):
                if encoded and not cls.is_pause(encoded[-1]):
                    encoded.append(word_pause)
                encoded.append(cls.parse_ansi(item))
            else:
                raise Exception('Passed item incorrect: ' + repr(item))
        if end_pause is not None and end_pause > 0.0:
            encoded.append(float(end_pause))
        return tuple(encoded)

    def print_item(self, s, char_pause:float=None):
        """s is tuple of pure strings or ANSI codes."""
        char_pause = self.char_pause if char_pause is None else char_pause
        if isinstance(s, str):
            for c in s:
                self.write_flush(c)
                self._pause(char_pause)
        elif isinstance(s, tuple):
            for item in s:
                if self.is_ansi(item):
                    self.write_flush(item)
                else:
                    for c in item:
                        self.write_flush(c)
                        self._pause(char_pause)
        else:
            raise Exception('Incorrect s: ' + repr(s))

    def print(self, char_pause:float=None, end=''):
        """Animated print of self."""
        self.char_pause = float(char_pause) if char_pause is not None else self.char_pause
        for item in self.string:
            if self.is_pause(item):
                self._pause(self.word_pause)
            else:
                self.print_item(item, char_pause)
        print(end, end='')


class IntonatedStringSequence:
    base_type = IntonatedString

    def __init__(self, frames=None, iterator=cycle, duration:float=None, fps:int=None):
        """
        prompt is constant string
        frames is finite collection of str or IntonatedStrings without pauses!
        iterator is infinite iterator for looped print
        """
        base_type = IntonatedStringSequence.base_type
        self.frames = []
        for f in frames:
            if isinstance(f, str):
                self.frames.append(base_type(f))
            elif isinstance(f, base_type):
                self.frames.append(f)
            else:
                raise ValueError('Invalid frame: ' + repr(f))
        self.frames = tuple(self.frames)
        self.frames_infinite = iterator(self.frames)
        self.duration = float(duration) if duration is not None else 5.0
        self.fps = int(fps) if fps is not None else 5

    def __str__(self):
        self.print()
        return ''

    @classmethod
    def _clean_stdout(cls, length:int):
        """Removes last length characters from stdout."""
        ret = '\b' * length
        clean = ' ' * length
        IntonatedString.write_flush(ret, clean, ret)

    def print_looped(self, prompt=None, duration:float=None, fps:int=None):
        """Pauses are ignored."""
        duration = float(duration) if duration is not None else self.duration
        fps = int(fps) if fps is not None else self.fps

        if prompt:
            print(prompt, end='')

        pause = 1.0 / fps
        tstart = time.time()
        frame = ''
        written = 0
        while time.time() - tstart < duration:
            frame = next(self.frames_infinite)
            for part in frame.unzip():
                if self.base_type.is_ansi(part):
                    sys.stdout.write(part)
                elif self.base_type.is_pause(part):
                    pass
                else:
                    written += self.base_type.write_flush(part)

            time.sleep(pause)
            self._clean_stdout(written)
            written = 0
        
        if prompt:
            self._clean_stdout(len(prompt))

    def print(self, pause=0, end_pause=0, sep=' ', end=''):
        for i, frame in enumerate(self.frames):
            print(frame, end=sep)
            if pause > 0 and i < len(self.frames)-1:
                time.sleep(pause)
        
        if end_pause > 0:
            time.sleep(end_pause)
        
        print(end=end)

