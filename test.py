import urllib
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp
from states import Service1
from loader import bot
from data.config import BOT_TOKEN




@dp.message_handler(content_types=['document'], state=NewUserStart.get_zip_data)
async def scan_message(msg: types.Message, state: FSMContext):
    document_id = msg.document.file_id
    file_info = await bot.get_file(document_id)

    print('file info'*100)
    print(file_info)

    fi = file_info.file_path
    name = msg.document.file_name
    urllib.request.urlretrieve(f'https://api.telegram.org/file/bot{BOT_TOKEN}/{fi}',f'./media/{name}')
    await bot.send_message(msg.from_user.id, 'Файл успешно сохранён')

    # with open('media/result.jpg', 'rb') as f:
    #     await bot.send_document(chat_id=409524113, document=f)

    with open(f'media/{name}', 'rb') as f:
        await bot.send_document(chat_id=409524113, document=f)

    await state.finish()
