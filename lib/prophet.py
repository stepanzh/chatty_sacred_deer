from lib.core.intonated_string import IntonatedStringSequence, IntonatedString
from lib.core.colors import Colors, color

from lib.utils import StopTalking, randcycle
from lib.message_parser import MessageParser, SENT_TYPE_QUESTION, SENT_TYPE_EMPHASIS, SENT_TYPE_NEUTRAL
from lib.character import AbstractCharacter, Character, DefaultCharacter, TestCharacter

from collections import deque

import sys, time, random

class Comandable:
    _cmd_bye = 'пока-пока'
    _cmd_help = 'помощь'
    _cmd_color = color(82)

    def _is_cmd_bye(self, s):
        return s.strip().lower().startswith(self._cmd_bye)

    def _is_cmd_help(self, s):
        return s.strip().lower() == self._cmd_help

    def print_help(self):
        cpause = 0.04
        print(IntonatedString('  Я умею отвечать на вопросы и болтать.', char_pause=cpause))
        print()
        print(
            IntonatedString(
                Colors.colorise('  Вопрос мне должен оканчиваться на ', Colors.pink),
                Colors.colorise('?', self._cmd_color),
                word_pause=0, char_pause=cpause
            )
        )
        print(
            IntonatedString(
                '  Постарайся спрашивать то, на что можно ответить да или нет.',
                char_pause=cpause
            )
        )
        print()
        print(IntonatedString('  Чтобы пообщаться, скажи мне что угодно.', char_pause=cpause))
        print(
            IntonatedString(
                Colors.colorise('  Я точно обращу на тебя внимание, если твоё сообщение оканчивается восклицательным знаком', Colors.pink),
                Colors.colorise(' !', self._cmd_color),
                word_pause=0, char_pause=cpause
            )
        )
        print()
        print(
            IntonatedString(
                '  Чтобы попращаться, скажи мне ',
                Colors.colorise('Пока-пока', self._cmd_color),
                word_pause=0, char_pause=cpause
            )
        )


class Prophet(AbstractCharacter, Comandable):
    reply_type_answer = 'answer'
    reply_type_emotion = 'emotion'

    def __init__(self, character:Character=DefaultCharacter):
        Character.__init__(self, character=character)
        # Comandable.__init__(self)

        self.reply_query = deque()
        self.think_sequence = IntonatedStringSequence(
            frames=self.get_think_frames(),
            iterator=randcycle
        )

    def _think(self):
        self.think_sequence.print_looped(
            prompt=self.choice_think_prompt(),
            duration=self.think_duration(),
            fps=7
        )

    def answer(self, a, end='\n'):
        print(a, end=end)

    def emote(self, e, end='\n'):
        print(e, end=end)

    def listen(self, s):
        s = s.strip().lower()
        
        if self._is_cmd_bye(s):
            self.bye()
            raise(StopTalking())
        elif self._is_cmd_help(s):
            self.print_help()
        else:
            for sentence in MessageParser.sentences(s):
                s_type = MessageParser.sentence_type(sentence)
                if s_type == SENT_TYPE_QUESTION:
                    self.reply_query.append((self.reply_type_answer, self.choice_answer(sentence)))
                elif s_type == SENT_TYPE_EMPHASIS:
                    self.reply_query.append((self.reply_type_emotion, self.choice_emotion(sentence)))
                elif s_type == SENT_TYPE_NEUTRAL:
                    if self.want_emote():
                        self.reply_query.append((self.reply_type_emotion, self.choice_emotion(sentence)))
                else:
                    raise Exception('Unknown sentence type!')

            self._dump_reply_query()

    def _dump_reply_query(self):
        need_end = bool(self.reply_query)
        while self.reply_query:
            reply_type, reply = self.reply_query.popleft()
            if reply_type == self.reply_type_answer and self.want_think():
                self._think()
            print(reply, ' ', sep='', end='')
        
        if need_end:
            print()

    def _dump_answers(self, answers):
        if len(answers) and self.want_think():
            self._think()
        for a in answers:
            self.answer(a)

    def _dump_emotions(self, emotions):
        for e in emotions:
            self.emote(e)

    def welcome(self, w=None):
        w = w if w is not None else self.choice_welcome()
        print(w)

    def bye(self, bye_msg:str=None):
        bye_msg = bye_msg if bye_msg is not None else self.choice_bye()
        print(bye_msg)


DefaultProphet = Prophet(DefaultCharacter)
TestProphet = Prophet(TestCharacter)
