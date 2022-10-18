from aiogram.dispatcher.filters.state import StatesGroup, State

class Dowload(StatesGroup):
    dowload = State()

    '''
    Мы наследуем класс от StatesGroup и передаём внутрь полей класса объекты класса State.
    '''