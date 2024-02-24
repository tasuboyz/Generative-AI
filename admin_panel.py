from config import admin_id
from instance import bot 
from aiogram import types
from user import UserInfo
from aiogram.enums import ParseMode
from chat_keyboards import Keyboard_Manager
from state import Form
from aiogram.fsm.context import FSMContext
from db import Database
from logger_config import logger

class ChannelManager():
    def __init__(self):
        self.channel_id = -1002100731393
        self.keyboards = Keyboard_Manager()
        self.db = Database()
        pass

    async def admin_command(self, message: types.Message, state: FSMContext):
        info = UserInfo(message)
        chat_id = UserInfo(message)
        if info.caption_text:
            keyboard = self.keyboards.inline_keyboard_for_admin()
            caption_text = info.caption_text
            #await message.edit_caption(caption=caption_text, reply_markup=keyboard)
            await state.set_state(Form.attend_admin_text)
            await message.send_copy(admin_id, reply_markup=keyboard)
        #await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f"`{prompt}`\n(0)", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)       
        #await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f"`{prompt}`\n(0)", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        return
    
    async def edit_to_markdown(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        caption_text = info.caption_text
        start_index = caption_text.find('"')

        end_index = caption_text.find('"', start_index + 1)

        prompt = caption_text[start_index + 1:end_index]
        parameter = caption_text[end_index + 1:]

        caption_text = f"`{prompt}`\n {parameter}"
        keyboard = self.keyboards.send_to_channel_keyboard()
        await callback_query.message.edit_caption(caption=caption_text, parse_mode=ParseMode.MARKDOWN, reply_markup=keyboard)

    async def send_to_leonardo(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        chat_id = info.chat_id
        message_id = info.message_id
        msg = await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)
        await msg.send_copy(self.channel_id)
        return
    
    async def admin_keyboard(self, message: types.Message):
        info = UserInfo(message)
        user_id = info.user_id
        if user_id == admin_id:
            keyboard = self.keyboards.admin_keyboard()
            await message.answer("Panel:", reply_markup=keyboard)
        return
    
    async def give_to_user(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        data = info.user_data
        try:
            async for user_id in Database().get_users():
                token = self.db.user_token(user_id[0])
                token += 10               
                try:
                    await bot.send_message(user_id[0], "Owner give you +10🪙, thanks for testing!")
                    self.db.update_user_token(token, user_id[0])
                except Exception as ex:
                    await bot.send_message(admin_id, f"{ex}")
                    logger.error(ex)
            return
        except Exception as ex:
            await bot.send_message(admin_id, f"{ex}")
            logger.error(ex)
