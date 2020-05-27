SENT_TYPE_QUESTION = 'question'
SENT_TYPE_EMPHASIS = 'emphasis'
SENT_TYPE_NEUTRAL = 'neutral'


class MessageParser:
    narrative_term = '.'
    emphasis_term = '!'
    question_term = '?'
    sentence_terminators = narrative_term + question_term + emphasis_term

    @classmethod
    def sentences(cls, text):
        i = 0
        near_sentend = False

        for j, c in enumerate(text):
            if c in cls.sentence_terminators and not near_sentend:
                near_sentend = True
            elif c not in cls.sentence_terminators and near_sentend:
                yield text[i:j+1].strip()
                i = j+1
                near_sentend = False

            if j == len(text)-1:
                yield text[i:].strip()

    @classmethod
    def _get_terminator(cls, sentence):
        t = ''
        for c in reversed(sentence):
            if c in cls.sentence_terminators:
                t += c
        return t[::-1]

    @classmethod
    def _is_term_question(cls, term):
        return cls.question_term in term and cls.emphasis_term not in term

    @classmethod
    def _is_term_emphasis(cls, term):
        return cls.emphasis_term in term

    @classmethod
    def is_question(cls, sentence):
        term = cls._get_terminator(sentence)
        return cls._is_term_question(term)

    @classmethod
    def is_emphasis(cls, sentence):
        term = cls._get_terminator(sentence)
        return cls._is_term_emphasis(term)

    @classmethod
    def sentence_type(cls, sentence):
        term = cls._get_terminator(sentence)
        if cls._is_term_question(term):
            return SENT_TYPE_QUESTION
        elif cls._is_term_emphasis(term):
            return SENT_TYPE_EMPHASIS
        else:
            return SENT_TYPE_NEUTRAL


if __name__ == "__main__":
    s = 'Привет, Олень!   Как твои дела? Чем занимаешься?..   Да как так-то!??!? Ну, ладно!   Пока!    Пока? Вот-так то...'
    
    print('Sample:')
    print(repr(s))
    print()
    for sentence in MessageParser.sentences(s):
        print(repr(sentence))
        # print(" terminator {}".format(repr(MessageParser._get_terminator(sentence))))
        # print(" is_question:", MessageParser.is_question(sentence))
        # print(" is_emphasis:", MessageParser.is_emphasis(sentence))
        print(' ', MessageParser.sentence_type(sentence))

