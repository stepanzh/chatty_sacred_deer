import unittest
from lib.prophet import Prophet


class ProphetPhrasesTestCase(unittest.TestCase):
    def setUp(self):
        self.prophet = Prophet()

    def test_answer(self):
        for a in self.prophet.get_answers():
            self.prophet.answer(a)

    def test_bye(self):
        for b in self.prophet.get_byes():
            self.prophet.bye(b)

    def test_welcome(self):
        for w in self.prophet.get_welcomes():
            self.prophet.welcome(w)

    def test_emote(self):
        for e in self.prophet.get_emotions():
            self.prophet.emote(e)

    def test_think_phrase(self):
        for prompt in self.prophet.get_think_prompts():
            for frame in self.prophet._think_frames:
                print(prompt, frame, sep='')

    def test_think(self):
        self.prophet._think()

    def test_help(self):
        self.prophet.print_help()
