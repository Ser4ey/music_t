import urllib

from service_date import ServiceDate

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from loader import dp
from keyboards.default import ServiceChooseMenu
from states import Service1, ServiceGlobal
from loader import bot
from data.config import BOT_TOKEN, admins


def formatting_user_data(user_data: dict):
    user_text = 'Новая заявка:\n\n'
    try:
        user_id = user_data.get('user_id')
        user_text += f'ID пользователя: {user_id}\n'
    except:
        pass

    try:
        user_name = user_data.get('user_name')
        user_text += f'Имя пользователя: @{user_name}\n'
    except:
        pass

    for k, v in user_data.items():
        if k != 'user_id' and k != 'user_name' and k != 'scenario' and k != 'step':
            user_text += f'{k}: {v}\n'
    return user_text


async def do_scenario_step(message: types.Message, state: FSMContext):
    message_text = message.text

    data_ = await state.get_data()
    # print(data_.get('scenario'))
    my_service = ServiceDate[data_.get('scenario')]

    step_work = my_service['history'].get(data_.get('step'))
    text, menu, next_step, data_name = step_work.return_result(message_text)

    if data_name != '':
        await state.update_data({data_name: message_text})

    # прекращение работы
    if next_step == 'kill_service':
        await message.answer(text=text, reply_markup=ServiceChooseMenu)
        await state.finish()
        # отправка уведомлений о заявке админам
        # for admin in admins:
        #     await bot.send_message(admin, formatting_user_data(data_))
        return


    await message.answer(text=text, reply_markup=menu)

    if next_step == 'end':
        await ServiceGlobal.end_work.set()
        print('end of work')

    await state.update_data(step=next_step)
    # await message.answer(str(await state.get_data()))


@dp.message_handler()
async def service1_(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.username
    text = message.text
    scenario = -1
    step = '0'

    await ServiceGlobal.history_work.set()

    for i in range(len(ServiceDate)):
        service_ = ServiceDate[i]
        if service_['name'] == text:
            scenario = i
            break
    if scenario == -1:
        await state.finish()
        await message.answer('Неизвестная услуга', reply_markup=ServiceChooseMenu)
        return

    await state.update_data(user_id=user_id)
    await state.update_data(user_name=user_name)
    await state.update_data(scenario=scenario)
    await state.update_data(step=step)

    await ServiceGlobal.history_work.set()

    await do_scenario_step(message, state)


@dp.message_handler(state=ServiceGlobal.history_work)
async def service1_(message: types.Message, state: FSMContext):
    await do_scenario_step(message, state)


@dp.message_handler(state=ServiceGlobal.end_work)
async def service1_(message: types.Message, state: FSMContext):
    message_text = message.text

    data_ = await state.get_data()
    # print(data_.get('scenario'))
    my_service = ServiceDate[data_.get('scenario')]

    agree_answer = my_service['history'].get('agree_step')

    if message_text == 'Отправить заявку':
        await message.answer(agree_answer, reply_markup=ServiceChooseMenu)
        await state.finish()
        # отправка уведомлений о заявке админам
        for admin in admins:
            await bot.send_message(admin, formatting_user_data(data_))

    else:
        await message.answer('Вы отменели вашу заявку!', reply_markup=ServiceChooseMenu)
        # await message.answer(str(await state.get_data()))
        await state.finish()


# Сохранение и отправка файла
@dp.message_handler(content_types=['document'])
async def scan_message(message: types.Message, state: FSMContext):
    user_name = message.from_user.username

    document_id = message.document.file_id

    try:
        file_info = await bot.get_file(document_id)
    except Exception as er:
        print('Ошибка при загрузке файла:', er)
        await message.answer('Максимальный размер файла 20МБ')
        await state.finish()
        return
    # data_ = await state.get_data()
    # my_service = ServiceDate[data_.get('scenario')]
    # agree_answer = my_service['history'].get('agree_step')

    await state.finish()
    # await bot.send_message(message.from_user.id, agree_answer, reply_markup=ServiceChooseMenu)
    fi = file_info.file_path
    name = message.document.file_name
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{fi}',f'./media/{name}')
    await bot.send_message(message.from_user.id, 'Файл успешно получен')

    with open(f'media/{name}', 'rb') as f:
        for admin in admins:
            # await bot.send_message(admin, formatting_user_data(data_))
            await bot.send_message(admin, f'''
Файл от пользователя

Имя пользователя: @{user_name}
Имя файла: {name}
''')
            await bot.send_document(chat_id=admin, document=f)




