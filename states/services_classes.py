from aiogram.dispatcher.filters.state import StatesGroup, State


class ServiceGlobal(StatesGroup):
    history_work = State()
    end_work = State()


class Service1(StatesGroup):
    choose_date = State()
    choose_time = State()

    choose_hhmm_time = State()

    end_ = State()

class Service2(StatesGroup):
    get_special_type_of_service = State()
    get_date_time = State()
    get_zip_data = State()


class Service3(StatesGroup):
    get_special_type_of_service = State()
    get_date_time = State()
    get_zip_data = State()


class Service4(StatesGroup):
    get_special_type_of_service = State()
    get_date_time = State()
    get_zip_data = State()

