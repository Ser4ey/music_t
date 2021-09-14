from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ServiceChooseMenu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Запись 🎤'),#1
        ],
        [
            KeyboardButton(text='Сведение 🎛'),#2
        ],
        [
            KeyboardButton(text='Мастеринг 🎚'),#3
        ],
        [
            KeyboardButton(text='Стем-мастеринг 🎚'),#4
        ],
        [
            KeyboardButton(text='Снятие аранжировки 🎸'),#5
        ],
        [
            KeyboardButton(text='Эксклюзивный бит 🧨'),#6
        ],
        [
            KeyboardButton(text='Эксклюзивный минус 🎹'),#7
        ],
        [
            KeyboardButton(text='Создание бита или минуса с аранжировщиком на студии 🎹'),#8
        ],
        [
            KeyboardButton(text='Готовый бит 🧨'),#9
        ],
        [
            KeyboardButton(text='Готовый минус 🎧'),#10
        ],
        [
            KeyboardButton(text='Звуковое оформление (Саунд дизайн) 🎻'),#11
        ],
        [
            KeyboardButton(text='Озвучка 🎤🎧'),#12
        ],
        [
            KeyboardButton(text='Съёмка видео. 🎬'),#13
        ],

    ],
    resize_keyboard=True
)


# 1 service
s1_text1 = 'Почасовая запись ⏰'
s1_text2 = 'День на студии 🌞'
s1_text3 = 'Ночь на студии 🪐'
ServiceMenu1 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=s1_text1),
        ],
        [
            KeyboardButton(text=s1_text2),
        ],
        [
            KeyboardButton(text=s1_text3),
        ],


    ],
    resize_keyboard=True
)


# 2 service
s2_text1 = 'Минус одной дорожкой 🎵'
s2_text2 = 'Раскладка минуса (Track out) 🎶'
s2_text3 = 'PRO 🔝'
ServiceMenu2 = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=s2_text1),
        ],
        [
            KeyboardButton(text=s2_text2),
        ],
        [
            KeyboardButton(text=s2_text3),
        ],


    ],
    resize_keyboard=True
)

AgreeMenu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Отправить заявку'),
            KeyboardButton(text='Отмена'),
        ],



    ],
    resize_keyboard=True
)

