from lib.core.colors import Colors, color
from lib.core.intonated_string import IntonatedString
from lib.core.rarity import *


answer_color = Colors.boldwhite

# reaction must be tuple of 2-sized tuple (w, s)
#  where w is relative weight of probability
#        s is str (without ansi) or IntonatedString

default_answers = (
    (Normal.w, IntonatedString(
            Colors.colorise('Да', answer_color),
            Colors.colorise('.', answer_color),
            end_pause=True
        )
    ),
    (Normal.w, IntonatedString(Colors.colorise('Нет.', answer_color))),
    (Normal.w, IntonatedString(
            Colors.colorise('Это...', answer_color),
            Colors.colorise(' не важно.', answer_color)
        )
    ),
    (Normal.w, IntonatedString(Colors.colorise('Спокойно, друг.', answer_color))),
    (Normal.w, IntonatedString(
            Colors.colorise('Это...', answer_color),
            Colors.colorise(' сарказм!?', answer_color)
        )
    ),
    (Normal.w, IntonatedString(
            Colors.colorise('Да', answer_color),
            Colors.colorise(', хотя зря.', answer_color)
        )
    ),
    (Normal.w, IntonatedString(
            Colors.colorise('Ни', answer_color),
            Colors.colorise('ког', answer_color),
            Colors.colorise('да!', answer_color),
            end_pause=True
        )
    ),
    (Normal.w, IntonatedString(Colors.colorise('100%', answer_color))),
    (Normal.w, IntonatedString(
            Colors.colorise('Шанс...', answer_color),
            Colors.colorise(' 1 из 100.', answer_color)
        )
    ),
    (Normal.w, IntonatedString(Colors.colorise('Ещё разок.', answer_color))),
    (Unique.w, IntonatedString(
            Colors.colorise('Veni,', color(190)),
            Colors.colorise(' vidi,', color(190)),
            Colors.colorise(' vici', color(190))
        ),
    ),
)
default_emotions = (
    (Normal.w, IntonatedString(Colors.colorise('Ага.', Normal.c))),
    (Normal.w, IntonatedString(Colors.colorise(':)', Normal.c))),
    (Normal.w, IntonatedString(Colors.colorise('Ну...', Normal.c))),
    (Rare.w, IntonatedString(Colors.colorise('...', Rare.c))),
    (Rare.w, IntonatedString(
            Colors.colorise('О', Rare.c),
            Colors.colorise('К', Rare.c),
            end_pause=True
        )
    ),
    (Rare.w, IntonatedString(Colors.colorise('¡No pasarán!', Rare.c))),
    (VRare.w, IntonatedString(
            Colors.colorise('Звучит...', VRare.c),
            Colors.colorise(' серьёзно.', VRare.c)
        )
    ),
    (VRare.w, IntonatedString(Colors.colorise('Смешно.', VRare.c))),
    (Extreme.w, IntonatedString(Colors.colorise('Серьёзно?!...', Extreme.c))),
    (Extreme.w, IntonatedString(Colors.colorise('C\'est la vie.', Extreme.c))),
    (Legend.w, IntonatedString(Colors.colorise('АХАХaXAХaх', Legend.c))),
    (Legend.w, IntonatedString(Colors.colorise('Смерть неверным!', Colors.red))),
    (Unique.w, IntonatedString(
            Colors.colorise('Пивкааа', Colors.orange),
            Colors.rainbow(' для рывка!'),
            end_pause=True
        )
    ),
    (Unique.w, IntonatedString(Colors.rainbow('Что-то случилось в наших лесах!'))),
)
default_welcomes = (
    (Normal.w, IntonatedString('Привет!')),
    (Normal.w, IntonatedString('Добрый день.')),
    (Normal.w, IntonatedString('Здравствуй.')),
    (Normal.w, IntonatedString('Здравия желаю.')),
    (Rare.w, IntonatedString(
            Colors.colorise('Ну и погодка...', Rare.c),
            ' Привет.'
        )
    ),
    (Rare.w, IntonatedString(
            Colors.colorise('Аааа когда на море качка, ты приходи ко мне...', Rare.c),
            ' Привет.'
        )
    ),
    (VRare.w, IntonatedString(
            Colors.colorise('Ну чтоооооо ещё?', VRare.c),
        )      
    ),
    (VRare.w, IntonatedString(Colors.colorise('Однажды мне тоже прострелили колено.', VRare.c), ' Привет!')),
    (Legend.w, IntonatedString(Colors.colorise('Она просто сумасшедшая в постели. Оу.', Colors.pink), ' Здравствуй!')),
    (Legend.w, IntonatedString(
            Colors.colorise('Поговаривают о мужике, купившем шляпу...', Legend.c),
            Colors.colorise(' Ты не слышал?', Legend.c),
        ),
    ),
    (Unique.w, IntonatedString(
            Colors.colorise('Я не видел женщин', color(199)),
            Colors.colorise(' уже десять', color(198)),
            Colors.colorise(' тысяч', color(197)),
            Colors.colorise(' лет!!!', color(196)),
            ' Здравствуй!'
        )
    ),
)
default_byes = (
    (Normal.w, IntonatedString('Пока-пока!')),
    (Normal.w, IntonatedString('Прощай, дружище!')),
    (Normal.w, IntonatedString('Ещё увидимся!')),
    (Legend.w, IntonatedString(
            Colors.colorise('Ну и на это всё :)', Legend.c),
            Colors.colorise(' До новых встреч :<', Legend.c),
        )
    ),
    (Unique.w, IntonatedString(Colors.rainbow('Я всегда рядом.'), ' Хех.')),
)
default_think_prompts = (
    (Normal.w, IntonatedString('Дай-ка подумать... ')),
    (Normal.w, IntonatedString('Хмммм... ')),
    (Normal.w, IntonatedString('Секунду... ')),
)
default_think_frames = ( # no pauses!
    '!%@#?.вы',
    'купил мужик шляпу', 'а она ему как раз',
    IntonatedString(Colors.colorise('φιλοσοφία', Colors.purple)),
    IntonatedString(Colors.colorise('εὕρηκα', Colors.yellow)),
    IntonatedString(Colors.colorise('хвост_мышки_майкрософт', Colors.lightblue)),
    IntonatedString('+воспалённая ' + Colors.rainbow('фантазия') + '+'),
    '----Жизнь-игра----',
    'я белка-страшный зверь',
    IntonatedString(Colors.rainbow('_ДеVо4к@,kOтO®Aя )(оТеЛ@ ©4@$tьЯ')),
)
