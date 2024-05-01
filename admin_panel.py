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
import asyncio
import instance

class ChannelManager():
    def __init__(self):
        self.channel_id = -1002100731393
        self.keyboards = Keyboard_Manager()
        self.db = Database()
        self.bot = instance.bot
        pass

    async def admin_command(self, message: types.Message, state: FSMContext):
        info = UserInfo(message)
        chat_id = UserInfo(message)
        caption_text = message.caption
        try:
            if caption_text:
                keyboard = self.keyboards.inline_keyboard_for_admin()
                #await message.edit_caption(caption=caption_text, reply_markup=keyboard)
                #await state.set_state(Form.attend_admin_text)
                await message.send_copy(admin_id, reply_markup=keyboard)
        #await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f"`{prompt}`\n(0)", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)       
        #await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f"`{prompt}`\n(0)", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
        except Exception as ex:
            await bot.send_message(admin_id, f"{ex}")
            logger.error(ex)

    async def edit_to_markdown(self, callback_query: types.CallbackQuery):
        caption_text = callback_query.message.caption
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
        db = Database()
        user_id = info.user_id
        if user_id == admin_id:
            enable = db.get_enabled_mode(admin_id)
            keyboard = self.keyboards.admin_keyboard(enable)
            await message.answer("Panel:", reply_markup=keyboard)
        return
    
    async def give_to_user(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        chat_id = info.chat_id
        data = info.user_data
        message_id = info.message_id
        db = Database()
        count = 0
        user_blocked = []
        try:
            async for user_id in db.get_users():
                token = self.db.user_token(user_id[0])
                token += 1              
                try:
                    # if user_id[0] == admin_id:
                    #     continue            
                    channel = f'<a href="https://t.me/ClickBeeBot?start=1026795763">Join to earn TRX 🤑</a>'        
                    await bot.send_message(user_id[0], channel)
                    self.db.update_user_token(token, user_id[0]) 
                    await self.bot.edit_message_text(text=f"{count}", chat_id=chat_id, message_id=message_id)
                    count += 1
                    await asyncio.sleep(0.4)
                except Exception as ex:
                    user_blocked.append(user_id[0])
                    #await bot.send_message(admin_id, f"{ex}")
                    logger.error(ex)
            return
        finally:
            try:
                db.delate_user(user_ids=user_blocked)
            except Exception as ex:
                    await bot.send_message(admin_id, f"{ex}")
                    logger.error(ex)

    async def reset_contest(self, callback_query: types.CallbackQuery):
        db = Database()
        db.reset_competition()
        await callback_query.message.answer("Competizione resettata!")
        return
    
    async def count_users(self, callback_query: types.CallbackQuery):
        db = Database()
        count = db.count_users()
        await callback_query.message.answer(text=f"{count}")
        return
    
    async def recive_ads(Self, callback_query: types.CallbackQuery, state: FSMContext):
        await state.set_state(Form.set_ads)
        await callback_query.message.answer("Send me ads:")
    
    async def send_ads(self, message: types.Message, state: FSMContext):
        info = UserInfo(message)
        ads = message.text
        db = Database()
        await state.clear()
        count = 0
        id_da_escludere = db.get_payed_user()
        id_to_delate = []
        try:
            async for user_id in db.get_users():
                if user_id[0] in id_da_escludere:
                   continue
                #if count == 5111:
                #    logger.error(f"Completed!")
                #    break
                try:
                    await asyncio.sleep(0.4)
                    await message.send_copy(user_id[0])
                    logger.error(f"{user_id[0]} Sended! {count}")
                    count += 1
                except Exception as e:             
                    #logger.error(f"{user_id[0]}, delated \n{e}") 
                    id_to_delate.append(user_id[0])
        finally:
            try:
                for user_id in id_to_delate:
                    Database().delate_ids(user_id)      
                    logger.error(f"Completed!")     
            except Exception as e:             
                    logger.error(f"{user_id[0]}, delated \n{e}") 

    async def leonardo_mode_enabled(self, callback_query: types.CallbackQuery):
        info = UserInfo(callback_query)
        db = Database()
        message_id = info.message_id
        try:
            enabled = db.get_enabled_mode(admin_id)
            if enabled:
                enabled = False
                db.insert_enable_mode(admin_id, enabled)
            else:
                enabled = True
                db.insert_enable_mode(admin_id, enabled)            
            keyboard = self.keyboards.admin_keyboard(enabled)
            await callback_query.message.edit_reply_markup("message_id", reply_markup=keyboard)
        except Exception as e:             
            logger.error(f"{e}", exc_info=True) 