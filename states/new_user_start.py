from aiogram.dispatcher.filters.state import StatesGroup, State


class NewUserStart(StatesGroup):
    get_special_type_of_service = State()
    get_date_time = State()
    get_zip_data = State()



