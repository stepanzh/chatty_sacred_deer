import unittest

from lib.core.intonated_string import IntonatedString, IntonatedStringSequence
from lib.core.colors import Colors

simple = IntonatedString('I\'m simple string.')
colored = IntonatedString(Colors.colorise('I\'m red string.', Colors.red))
rainbow = IntonatedString(Colors.rainbow('I\'m rainbow string.'))
paused = IntonatedString('Before default pause', ' after pause, before long pause', 2, ' after long pause')
paused_rainbow = IntonatedString(Colors.rainbow('I\'m rainbow string, before default pause'), ' after pause')
paused_end = IntonatedString('I\'m simple string with pause at end.', end_pause=True)


class IntonatedStringTest(unittest.TestCase):
    def setUp(self):        
        self.intons = [
            simple, 
            colored,
            rainbow,
            paused,
            paused_rainbow,
            paused_end
        ]

    def test_print(self):
        for inton in self.intons:
            # print(repr(inton))
            print(inton)

class IntonatedStringSequenceTest(unittest.TestCase):
    def setUp(self):
        self.inton_seq = IntonatedStringSequence(
            frames=[simple, colored],
            duration=4,
            fps=2,
        )
    def test_looped(self):
        self.inton_seq.print_looped(prompt='Prompt string ')

    def test_print(self):
        self.inton_seq.print(pause=1, end='\n')
        print(self.inton_seq)
