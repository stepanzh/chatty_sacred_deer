from lib.prophetview import ProphetView, TextIntonationDecoder
from lib.utils import Colors
from itertools import cycle

import unittest, sys, os


class ProphetViewTestCase(unittest.TestCase):
    def setUp(self):
        self.view = ProphetView
        self.idec = self.view.intonation_decoder
        
        self.pause_code = self.idec.get_pause_code()
        self.color = '\u001b[32;1m'
        
        p = self.pause_code
        c = self.color
        self.phrases = [
            'Здесь нет пауз, это одна строка',
            self.idec.parse('Здесь'+p+' две'+p+' паузы'),
            self.idec.parse('Одна пауза'+p+c+' и другой цвет')
        ]

    def test_intonated_print(self):
        for p in self.phrases:
            self.view.intonated_print(p, need_cr=True, wpause=0.3, cpause=0.02)

    def test_print_and_clean(self):
        p = 'Я появлюсь и сотрусь.'
        self.view.intonated_print(p, need_cr=False)
        self.view._clean_stdout(len(p))
        self.view.intonated_print(p, need_cr=True)

    def test_looped(self):
        prompt = 'Prompt_string '
        frames = cycle([
            self.idec.parse('$*@&$!'),
            self.idec.parse(',admldaw'),
            self.idec.parse(Colors.rainbow('1kmk8d@12e0'))
        ])

        self.view.looped_print(prompt, frames, duration=5.0, fps=2)
        print('Check for cleared stdout')


class ParsingTestCase(unittest.TestCase):
    def setUp(self):
        self.idec = TextIntonationDecoder
        self.pause_code = self.idec.get_pause_code()

    def test_is_ansi(self):
        self.assertEqual(self.idec.is_color('\u001b[0m'), True)
        self.assertEqual(self.idec.is_color('\u001b[32;1m'), True)
        self.assertEqual(self.idec.is_color('\u001b[38;5;255m'), True)
        self.assertEqual(self.idec.is_color('privetm'), False)

    def test_parse_ansi(self):
        self.assertEqual(self.idec.parse_color('\u001b[32;1mPrivet'), ('\u001b[32;1m', 'Privet'))
        self.assertEqual(
            self.idec.parse_color('\u001b[32;1mPrivet\u001b[32;1m'),
            ('\u001b[32;1m', 'Privet', '\u001b[32;1m')
        )
        self.assertEqual(
            self.idec.parse_color('Privet\u001b[32;1mPrivet Privetmmm\u001b[32;1mPrib ad'),
            ('Privet', '\u001b[32;1m', 'Privet Privetmmm', '\u001b[32;1m', 'Prib ad')
        )

    def test_parse_pause(self):
        p = self.pause_code
        self.assertEqual(
            self.idec.parse_pause(p), (p,)
        )
        self.assertEqual(
            self.idec.parse_pause(p + p), (p, p)
        )
        self.assertEqual(
            self.idec.parse_pause('A'+p+'BCD'+p), ('A', p, 'BCD', p)
        )

    def test_parse_intonation(self):
        p = self.pause_code
        c = '\u001b[32;1m'
        self.assertEqual(
            self.idec.parse('A'+c+'B'+p+'C'+c+c+p),
            ('A', c, 'B', p, 'C', c, c, p)
        )
        self.assertEqual(
            self.idec.parse('A'),
            ('A',)
        )