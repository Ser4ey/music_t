from aiogram import types
from loader import dp


@dp.message_handler(text='Посмотреть пост')
async def get_task(message: types.Message):
    id = message.from_user.id
    name = message.from_user.full_name

    user_info = db_of_active_users.select_active_User(telegram_id=id)
    if user_info is None:
        await message.answer(f'Приветствую, {name}! Вам необходимо зарегистрироваться.\nВаш id: {id}')
        return

    task = db_of_dayly_tasks.give_actual_task_to_User(id)
    await message.answer(task)






