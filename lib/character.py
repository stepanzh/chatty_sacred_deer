import random

from lib.core.intonated_string import IntonatedString
from lib.core.colors import Colors
import lib.config as config


class AbstractCharacter:
    _answers=None
    _emotions=None
    _welcomes=None
    _byes=None
    _think_prompts=None
    _think_frames=None

    _emotion_rate = None
    _think_rate = None
    _think_duration = None

    def copy_character(self, c):
        self._answers = c._answers  # should be from get_<reactinon>
        self._emotions = c._emotions
        self._welcomes = c._welcomes
        self._byes = c._byes
        self._think_prompts = c._think_prompts
        self._think_frames = c._think_frames

        self._emotion_rate = c._emotion_rate
        self._think_rate = c._think_rate
        self._think_duration = c._think_duration

    def _get_weights(self, reaction_tuple):
        return tuple(map(lambda x: x[0], reaction_tuple))

    def _get_reaction(self, reaction_tuple):
        return tuple(map(lambda x: x[1], reaction_tuple))

    def get_welcomes(self):
        return self._get_reaction(self._welcomes)
    
    def get_answers(self):
        return self._get_reaction(self._answers)
    
    def get_emotions(self):
        return self._get_reaction(self._emotions)
    
    def get_byes(self):
        return self._get_reaction(self._byes)

    def get_think_prompts(self):
        return self._get_reaction(self._think_prompts)

    def get_think_frames(self):
        return self._think_frames

    def choice_reaction(self, reaction_tuple):
        return random.choices(
            self._get_reaction(reaction_tuple),
            weights=self._get_weights(reaction_tuple),
            k=1
        )[0]

    def choice_answer(self, question):
        return self.choice_reaction(self._answers)

    def choice_welcome(self):
        return self.choice_reaction(self._welcomes)

    def choice_bye(self):
        return self.choice_reaction(self._byes)

    def choice_emotion(self, to=''):
        return self.choice_reaction(self._emotions)

    def choice_think_prompt(self):
        return self.choice_reaction(self._think_prompts)

    def think_duration(self):
        return self._think_duration

    def want_think(self):
        return random.random() < self._think_rate 

    def want_emote(self):
        return random.random() < self._emotion_rate


class Character(AbstractCharacter):
    def __init__(self,
            character:AbstractCharacter=None,
            answers=None,
            emotions=None,
            welcomes=None,
            byes=None,
            think_prompts=None,
            think_frames=None,
            emotion_rate=1.0,
            think_rate=1.0,
            think_duration=2.0
        ):
        if not character:
            self._answers = answers
            self._emotions = emotions
            self._welcomes = welcomes
            self._byes = byes
            self._think_prompts = think_prompts
            self._think_frames = think_frames

            self._emotion_rate = emotion_rate  # from [0, 1.0) 1.0 means always emote
            self._think_rate = think_rate
            self._think_duration = think_duration
        else:
            self.copy_character(character)


DefaultCharacter = Character(
    answers=config.default_answers,
    emotions=config.default_emotions,
    welcomes=config.default_welcomes,
    byes=config.default_byes,
    think_prompts=config.default_think_prompts,
    think_frames=config.default_think_frames,
    emotion_rate=0.4,
    think_rate=0.4,
    think_duration=2.0,
)

TestCharacter = Character(
    answers=config.default_answers,
    emotions=config.default_emotions,
    welcomes=config.default_welcomes,
    byes=config.default_byes,
    think_prompts=config.default_think_prompts,
    think_frames=config.default_think_frames,
)

