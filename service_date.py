from keyboards.default import *
from aiogram.types import ReplyKeyboardRemove


URL_LOREM = 'https://2ip.ru'


def make_b(word):
    return '<b>' + str(word) + '</b>'


class RootHistoryStep:
    def __init__(self, data_name='', menu=ReplyKeyboardRemove()):
        self.menu = menu
        self.data_name = data_name
        self.next_step = 'end'
        self.text = '0'

    def return_result(self, message_text):
        return self.text, self.menu, self.next_step, self.data_name


class Service1_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = 'Введите день записи (4 марта)'
        self.next_step = '1'
        return self.text, self.menu, self.next_step, self.data_name


class Service1_1(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'День записи'
        self.text = 'Выберите время:'
        self.next_step = '2'
        return self.text, self.menu, self.next_step, self.data_name


class Service1_2(RootHistoryStep):
    '''Ответ от меню'''
    def return_result(self, message_text):
        self.menu = AgreeMenu
        if message_text == s1_text1:
            self.menu = ReplyKeyboardRemove()
            self.next_step = '2_1'
            self.text = f'''
{make_b('Стоимость')}: 500р (час)
{make_b('Описание')}: 60 минут на студии со звукорежиссёром.

-Введите промежуток времени в формате hh:mm-hh:mm (10:30-15:30).'''

        elif message_text == s1_text2:
            self.next_step = 'end'
            self.data_name = 'Время записи'
            self.text = f'''
{make_b('Стоимость')}: 2500
{make_b('Описание')}: 6 часов в промежутке (11:00-19:00) на студии со звукорежиссёром.
'''
        else:
            self.next_step = 'end'
            self.data_name = 'Время записи'
            self.text = f'''
{make_b('Стоимость')}: 2500
{make_b('Описание')}: 6 часов в промежутке (23:00-07:00) на студии со звукорежиссёром. 
            '''

        return self.text, self.menu, self.next_step, self.data_name


class Service1_2_1(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Время записи'
        self.text = 'Вы хотите оставить заявку?'
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text1 = '''
Отличный выбор! ✌️😎👍
Наш специалист свяжется с вами для уточнения деталей.
'''

# 2 сервис
class Service2_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = '- выберите сложность'
        self.next_step = '1'
        return self.text, self.menu, self.next_step, self.data_name


class Service2_1(RootHistoryStep):
    def return_result(self, message_text):
        self.text = 'some text'
        self.data_name = 'Сложность'
        self.next_step = 'end'

        if message_text == s2_text1:
            self.text = f'''
{make_b('Стоимость')}: 1500
{make_b('Результат')} через: 2-3 дня
{make_b('Описание')}: Приведение к качественному звучанию ваших записей вместе с одной дорожкой минуса + финализации аудио материала, доведение его до коммерческого уровня (мастеринг)
После окончания работы возможны 2 бесплатные редакции. Каждая следующая оплачивается отдельно
{make_b('Дополнительно')}: +1 человек в треке (1000р);
Ручная коррекция 1й дорожки вокала (500р)
Редактирование после окончания работ (500р одна редакция)
'''
        elif message_text == s2_text2:
            self.text = f'''
{make_b('Стоимость')}: 2500
{make_b('Результат через')}: 3-4 дня
{make_b('Описание')}: Приведение к качественному звучанию ваших записей вместе с дорожками минуса + финализации аудио материала, доведение его до коммерческого уровня (мастеринг).
После окончания работы возможны 2 бесплатные редакции. Каждая следующая оплачивается отдельно.

{make_b('Дополнительно')}: +1 человек в треке (1000р);
Ручная коррекция 1й дорожки вокала (500р)
Доведение трека после сведения на студии со звукорежиссёром (60 мин. - 500р)
Редактирование после окончания работ (500р одна редакция)
'''
        else:
            self.text = f'''
{make_b('Стоимость')}: 6000р
{make_b('Результат через')}: 5-7 дней
{make_b('Описание')}: Скурпулёзное Приведение к качественному звучанию ваших записей вместе с дорожками минуса + 2 часа на студии со звукорежиссёром после окончания основных работ по сведению для точного редактирования трека по вашим желаниям + финализация аудио материала, доведение его до коммерческого уровня (мастеринг). После окончания работы возможны 2 бесплатные редакции. Каждая следующая оплачивается отдельно.
{make_b('Дополнительно')}: +1 человек в треке (2000р);
Редактирование после окончания работ (500р одна редакция)
'''
        return self.text, self.menu, self.next_step, self.data_name


agree_text2 = '''
Отличный выбор!✌️😎👍
Отправьте ваши аудио материалы и референсы с комментариями архивом или вложением следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
Обращаем ваше 💥внимание💥 на то что качество оформление вашего аудио материала напрямую влияет на скорость работы. 
Убедительно просим вас присылать нам только понятно подписанные дорожки(название должно отражать содержание).
В бите приветствуется наличие темпа в названии. 
'''


# 3 сервис
class Service3_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b('Стоимость одной композиции')}: 1000р.
{make_b('Результат через')}: 2-3 дня
{make_b('Описание')}: Финализация трека после сведения, доведение его до коммерческого уровня. После окончания работы возможны 2 бесплатные редакции. Каждая следующая оплачивается отдельно.
{make_b('Дополнительно')}: Редактирование после окончания работ (500р одна редакция)
'''

        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text3 = '''
Отличный выбор!✌️😎👍
Отправьте ваши аудио материалы и референсы с комментариями архивом или вложением следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты.После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
'''


# 4 сервис
class Service4_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b('Стоимость одной композиции')}: 2000
{make_b("Результат через")}: 2-4 дня
{make_b("Описание")}: Финализация трека после сведения в раскладке по дорожкам, доведение его до коммерческого уровня. После окончания работы возможны 2 бесплатные редакции. Каждая следующая оплачивается отдельно.
{make_b("Дополнительно")}: Редактирование после окончания работ (500р одна редакция)
'''

        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text4 = '''
Отличный выбор!✌️😎👍
Отправьте ваши аудио материалы и референсы с комментариями архивом следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
Обращаем ваше внимание на то что качество оформление вашего аудио материала напрямую влияет на скорость работы. 
Убедительно просим вас присылать нам только понятно подписанные дорожки(название должно отражать содержание).
В бите приветствуется наличие темпа в названии. 
'''


# 5 сервис
class Service5_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b('Стоимость')}: 4000р
{make_b('Результат через')}: 2-4 дня.
{make_b('Описание')}: Перебьём бит, снимем аранжировку или мелодию с песни, а также вытащим звук или синтезируем для вас максимально похожий.
'''

        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text5 = '''
Отличный выбор!✌️😎
Отправьте референсы (ссылкой или вложением) с комментариями в сообщении. После прослушивания материала наш специалист свяжется с вами для уточнения деталей. 
'''


# 6 сервис
class Service6_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: 4000р
{make_b("Результат через")}: 2-4 дня.
{make_b("Описание")}: создадим для вас бит с нуля и передадим полные права на него.
'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text6 = '''
Отличный выбор!✌️😎
Отправьте референсы (ссылкой или вложением) с комментариями в сообщении. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
'''

# 7 сервис
class Service7_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: 4000р
{make_b("Результат через")}: 2-4 дня.
{make_b("Описание")}: Напишем для вас минус и передадим полные права на него.
'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text7 = '''
Отличный выбор!✌️😎
Отправьте референсы (ссылкой или вложением) с комментариями в сообщении. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
'''


# 8 сервис
class Service8_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: 6000р
{make_b("Результат")}: Сразу по окончанию сессии
{make_b("Описание")}: Совместное создание музыки с нуля вместе с аранжировщиком на студии.
{make_b("Длительность сессии")}: 4 часа
{make_b("Дополнительно")}: Продление сессии на 1 час 500р
При создании 2х или более аранжировок за сессию права на каждую следующую оплачиваются отдельно, +4000 за каждую композицию.
'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text8 = '''
Отличный выбор!✌️😎
наш специалист свяжется с вами для уточнения деталей.
'''

# 9 сервис
class Service9_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
Стоимость: от 0.
Выберете понравившейся вам биты в нашем магазине: {URL_LOREM}
Или из наших бесплатных битов: {URL_LOREM}
'''
        self.next_step = 'kill_service'
        return self.text, self.menu, self.next_step, self.data_name

# 10 сервис
class Service10_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
Стоимость: от 0.
Списание: Выберите минус из представленных в нашем магазине: {URL_LOREM}
Или из наших бесплатных минусов: {URL_LOREM}
'''
        self.next_step = 'kill_service'
        return self.text, self.menu, self.next_step, self.data_name


# 11 сервис
class Service11_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: от 1000р
{make_b("Результат через")}: 2-7 дней. В зависимости от сложности и объёма работ.
{make_b("Описание")}: Создадим любое музыкальное сопровождение ваших YouTube, Tiktok, Instagram каналов или других блогов. Запишем джинглы, Напишем музыку для рекламы или игры.'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text11 = '''
Отличный выбор!✌️😎
Отправьте ваши аудио материалы и референсы с комментариями архивом следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
'''


# 12 сервис
class Service12_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: от 2000р
{make_b("Результат через")}: 3-7 дней. В зависимости от сложности и объёма работ.
{make_b("Описание")}: Профессионально озвучим видео ролики, аудио книги, запишем приветствие для телефона.
'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text12 = '''
Отличный выбор!✌️😎
Отправьте ваши аудио и видео материалы, а также референсы с комментариями архивом следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.
'''

# 12 сервис
class Service13_0(RootHistoryStep):
    def return_result(self, message_text):
        self.data_name = 'Название услуги'
        self.text = f'''
{make_b("Стоимость")}: от 10000р
{make_b("Результат через")}: 2-3 недели
{make_b("Описание")}: профессиональная съёмка и монтаж сниппетов, клипов, рекламы.
'''
        self.next_step = 'end'
        return self.text, self.menu, self.next_step, self.data_name


agree_text13 = '''
Отличный выбор!✌️😎
Отправьте ваши аудио и видео материалы, а также референсы с комментариями архивом следующим сообщением боту, нам в телеграмм @ep_prod или на почту «Почта». Туда же приложите ваши контакты. После прослушивания материала наш специалист свяжется с вами для уточнения деталей.'''


# имена сервисов нужно так же менять в файле keyboards/default/service_choose.py
ServiceDate = [
    {#1
        'name': 'Запись 🎤',
        'history': {
            '0': Service1_0(),
            '1': Service1_1(menu=ServiceMenu1),
            '2': Service1_2(menu=AgreeMenu),
            '2_1': Service1_2_1(menu=AgreeMenu),
            'agree_step': agree_text1

        }
    },
    {#2
        'name': 'Сведение 🎛',
        'history': {
            '0': Service2_0(menu=ServiceMenu2),
            '1': Service2_1(menu=AgreeMenu),

            'agree_step': agree_text2
        }
    },
    {#3
        'name': 'Мастеринг 🎚',
        'history': {
            '0': Service3_0(menu=AgreeMenu),

            'agree_step': agree_text3
        }
    },
    {#4
        'name': 'Стем-мастеринг 🎚',
        'history': {
            '0': Service4_0(menu=AgreeMenu),

            'agree_step': agree_text4
        }
    },
    {#5
        'name': 'Снятие аранжировки 🎸',
        'history': {
            '0': Service5_0(menu=AgreeMenu),

            'agree_step': agree_text5
        }
    },
    {#6
        'name': 'Эксклюзивный бит 🧨',
        'history': {
            '0': Service6_0(menu=AgreeMenu),

            'agree_step': agree_text6
        }
    },
    {#7
        'name': 'Эксклюзивный минус 🎹',
        'history': {
            '0': Service7_0(menu=AgreeMenu),

            'agree_step': agree_text7
        }
    },
    {#8
        'name': 'Создание бита или минуса с аранжировщиком на студии 🎹',
        'history': {
            '0': Service8_0(menu=AgreeMenu),

            'agree_step': agree_text8
        }
    },
    {#9
        'name': 'Готовый бит 🧨',
        'history': {
            '0': Service9_0(menu=AgreeMenu),
        }
    },
    {#10
        'name': 'Готовый минус 🎧',
        'history': {
            '0': Service10_0(menu=AgreeMenu),
        }
    },
    {#11
        'name': 'Звуковое оформление (Саунд дизайн) 🎻',
        'history': {
            '0': Service11_0(menu=AgreeMenu),

            'agree_step': agree_text11
        }
    },
    {#12
        'name': 'Озвучка 🎤🎧',
        'history': {
            '0': Service12_0(menu=AgreeMenu),

            'agree_step': agree_text12
        }
    },
    {#13
        'name': ' Съёмка видео. 🎬',
        'history': {
            '0': Service13_0(menu=AgreeMenu),

            'agree_step': agree_text13
        }
    },
]





