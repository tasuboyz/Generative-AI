from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Form(StatesGroup):
    attend_admin_text = State()
    Image_VisualQR = State()
    set_selement =State()
    set_ads = State()
