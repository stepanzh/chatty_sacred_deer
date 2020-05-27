#!/usr/bin/env python3

from lib.core.colors import Colors, color
from lib.core.intonated_string import IntonatedString
from lib.chat import Chat
from lib.prophet import Prophet, Comandable
from lib.character import DefaultCharacter, TestCharacter

import sys, random, time

random.seed(time.time())


def print_help():
    print()
    print(
        IntonatedString(
            '  Я, ', Colors.colorise('Сакральный Олень', color(220)) + ',',
            ' готов выслушать и ответить на прошения!', ''),
    )
    print()
    print(
        IntonatedString(
            '  Чтобы поговорить',
            ' - позови: '+ __file__+'.',
            ' Затем попроси ' + Colors.colorise('помощь', Comandable._cmd_color) + '.',
            ''
        )
    )
    print(
        IntonatedString('  Задать один вопрос', ' - задай: {} <твой вопрос>'.format(__file__), '')
    )
    print()
    print(
        IntonatedString(
            '  Вопросы должны оканчиваться на знак ' + Colors.colorise('?', Comandable._cmd_color),
            ''
        )
    )
    print(
        IntonatedString('  Постарайся спрашивать то, на что можно ответить "да"" или "нет".', '')
    )
    print(
        IntonatedString(
            Colors.colorise('  Но не всё так просто.', color(50)),
            ''
        )
    )
    print()
    print(
        IntonatedString('  Я жду...', '', char_pause=0.08)
    )
    print()

def reply_once(t):
    try:
        P = Prophet()
        P.listen(t)
        Chat.end()
    except Exception as e:
        Chat.end(e)

def chat():
    try:
        P = Prophet(character=DefaultCharacter)
        C = Chat(P)
        C.run()
    except Exception as e:
        Chat.end(e)

if len(sys.argv) > 1:
    if sys.argv[1] in ('-h', '--help'):
        print_help()
    else:
        text = ' '.join(sys.argv[1:])
        reply_once(text)
else:
    chat()
