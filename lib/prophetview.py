# import sys, time


# class TextIntonationDecoder:
#     color_start = '\u001b'  # ansi code start
#     color_end = 'm'         # ansi code end
#     pause_code = '!pause'

#     @classmethod
#     def get_pause_code(cls):
#         return cls.pause_code

#     @classmethod
#     def parse_color(cls, s:str):
#         """Returns sequence of ansi codes and pure strings."""
#         parsed = []
#         p = ''
#         found_ansi = False
#         i = 0
#         while i < len(s):
#             c = s[i]
#             if c == cls.color_start:
#                 if p:
#                     parsed.append(p)
#                     p = ''
#                 while c != cls.color_end and i < len(s):
#                     c = s[i]
#                     p += c
#                     i += 1
#                 parsed.append(p)
#                 p = ''
#             else:
#                 while i < len(s):
#                     if s[i] != cls.color_start:
#                         p += s[i]
#                         i += 1
#                     else:
#                         break
#                 parsed.append(p)
#                 p = ''
#         return tuple(parsed)

#     @classmethod
#     def is_color(cls, s:str):
#         return s.startswith(cls.color_start) and s.endswith(cls.color_end)

#     @classmethod
#     def parse_pause(cls, s:str):
#         """Returns tuple of strings."""
#         pause = cls.pause_code
#         if s.find(pause) > -1:
#             parsed = []
#             for i, word in enumerate(s.split(pause)):
#                 if word:
#                     parsed.append(word)
#                 parsed.append(pause)

#             if not s.endswith(pause):  # remove extra !pause at end
#                 parsed.pop()
#         else:
#             parsed = (s,)
#         return tuple(parsed)

#     @classmethod
#     def is_pause(cls, s:str):
#         return s == cls.pause_code

#     @classmethod
#     def parse(cls, s:str):
#         parsed_pauses = cls.parse_pause(s)
#         parsed = []
#         for part in parsed_pauses:
#             parsed.extend(cls.parse_color(part))
#         return tuple(parsed)


# class ProphetView:
#     char_pause = 0.02
#     word_pause = 0.8
#     intonation_decoder = TextIntonationDecoder

#     """Defines printing utilities."""
#     @classmethod
#     def pause(cls, duration):
#         time.sleep(duration)

#     @classmethod
#     def intonated_print(cls, phrase:str, need_cr:bool=True, wpause:float=None, cpause:float=None):
#         """Phrase is intonation string."""
#         idec = cls.intonation_decoder
#         if isinstance(phrase, str):
#             if idec.is_pause(phrase) or idec.is_color(phrase):
#                 raise Exception('Passed color or pause code to print:' + repr(phrase))
#             else:
#                 cls._animated_print_str(phrase, cpause)
#         else:
#             wpause = cls.word_pause if wpause is None else wpause
#             for part in phrase:
#                 if idec.is_color(part):
#                     sys.stdout.write(part)
#                 elif idec.is_pause(part):
#                     time.sleep(wpause)
#                 else:
#                     cls._animated_print_str(part, cpause)
#         if need_cr:
#             print()

#     @classmethod
#     def _animated_print_str(cls, s:str, cpause:float=None):
#         cpause = cls.char_pause if cpause is None else cpause
#         for c in s:
#             sys.stdout.write(c)
#             sys.stdout.flush()
#             time.sleep(cpause)

#     @classmethod
#     def _clean_stdout(cls, length:int):
#         """Removes last length characters from stdout."""
#         sys.stdout.write('\b'*length)
#         sys.stdout.write(' ' *length)
#         sys.stdout.write('\b'*length)
#         sys.stdout.flush()

#     @classmethod
#     def looped_print(cls, prompt:str='', frames=None, duration:float=5.0, fps=5):
#         """Prints `<prompt><frame>` where <frame> changes inplace during duration (sec).
#         Print of <prompt> does not count to duration.
#         frames - must support next(), each item is str
#         """
#         cls._animated_print_str(prompt)

#         pause = 1.0 / fps
#         tstart = time.time()
#         frame = ''
#         written = 0
#         while time.time() - tstart < duration:
#             frame = next(frames)
#             for part in frame:
#                 if cls.intonation_decoder.is_color(part):
#                     sys.stdout.write(part)
#                 else:
#                     written += sys.stdout.write(part)
#                     sys.stdout.flush()
#             time.sleep(pause)
#             cls._clean_stdout(written)
#             written = 0

#         cls._clean_stdout(len(prompt) + written)
