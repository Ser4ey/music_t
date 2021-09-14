from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from loader import dp
from keyboards.default import ServiceChooseMenu
from states import NewUserStart


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    name = message.from_user.full_name
    id = message.from_user.id

    await message.answer(text=f'Добро пожаловать, {name}, я помогу вам оставить заявку и расскажу об услугах.',
                         reply_markup=ServiceChooseMenu)
    # await NewUserStart.send_hello_1.set()

