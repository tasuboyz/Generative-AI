import config

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.types.chat import Chat
from user import UserInfo
import instance
import uuid
import shutil
import os
import re
import time
from logger_config import logger
from chat_keyboards import Keyboard_Manager
from openai_req import Dall_E
from db import Database
import math
from voting import Voting
from language import Language
from aiogram.enums import ParseMode
from aiogram import types
from datetime import datetime, timedelta
import json
from admin_panel import ChannelManager
from state import Form
from vip_command import LeonardoCommand

class BOT():
    def __init__(self):
        self.dp = Dispatcher()
        #self.router = Router()
        self.bot = instance.bot
        self.admin_id = config.admin_id
        self.openai = Dall_E()
        self.voting = Voting()
        self.admin_panel = ChannelManager()
        self.keyboard = Keyboard_Manager()
        self.channel_username = config.channel_username
        self.channel_id = f"@{self.channel_username}"
        self.channel_url = f"https://t.me/{self.channel_username}"
        self.contest_time = config.contest_time
        self.blocked_users = instance.blocked_users 
        self.leonardo = LeonardoCommand()
        self.db = Database()
        #command
        self.dp.message(CommandStart())(self.command_start_handler)
        self.dp.message(Command('user'))(self.admin_panel.admin_keyboard)
        self.dp.message(Form.set_selement)(self.leonardo.set_element)
        self.dp.message(F.text)(self.recive_prompts)
        self.dp.callback_query(F.data == "send")(self.send_image_to_channel)
        self.dp.callback_query(F.data == "1.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "2.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "3.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "4.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "5.0")(self.voting.give_star)
        
        self.dp.callback_query(F.data == "token")(self.give_referral)
        self.dp.callback_query(F.data == "yes")(self.send_image_to_channel)
        self.dp.callback_query(F.data == "cancel")(self.cancel)
        self.dp.callback_query(F.data == "setting")(self.choose_lang)
        self.dp.callback_query(F.data.startswith('code'))(self.choosed_language)
        self.dp.callback_query(F.data == 'size')(self.leonardo.choose_size)
        self.dp.callback_query(F.data.startswith('size:'))(self.leonardo.recive_choosed_size)

        #admin command
        self.dp.callback_query(F.data == "modify")(self.admin_panel.edit_to_markdown)
        self.dp.callback_query(F.data == "send_to_leonardo")(self.admin_panel.send_to_leonardo)
        self.dp.callback_query(F.data == "give_to_user")(self.admin_panel.give_to_user)
        self.dp.callback_query(F.data == "reset_competition")(self.admin_panel.reset_contest)
        self.dp.callback_query(F.data == "user_number")(self.admin_panel.count_users)
        self.dp.callback_query(F.data == "ads")(self.admin_panel.recive_ads)
        self.dp.callback_query(F.data == "enable")(self.admin_panel.leonardo_mode_enabled)
        self.dp.message(Form.set_ads)(self.admin_panel.send_ads)

        self.dp.callback_query(F.data == "leonardo")(self.leonardo_ai)
        
        self.dp.message(F.from_user.id == self.admin_id)(self.admin_panel.admin_command)

        #leonardo command
        self.dp.inline_query()(self.leonardo.inline_query_handler)  
        self.dp.callback_query(F.data == 'alchemy')(self.leonardo.set_alchemy_photoreal)
        self.dp.callback_query(F.data == 'photoreal')(self.leonardo.set_alchemy_photoreal)
        self.dp.callback_query(F.data == 'confirm')(self.leonardo.confirm_prompt)
        self.dp.callback_query(F.data == '0.1')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.2')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.3')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.4')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.5')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.6')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.7')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.8')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '0.9')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '1')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.1')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.2')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.3')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.4')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.5')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.6')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.7')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.8')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-0.9')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == '-1')(self.leonardo.set_element_point)
        self.dp.callback_query(F.data == 'cancel_leonardo')(self.leonardo.cancel_operation)
        self.dp.callback_query(Form.set_selement, F.data == 'cancel_element')(self.leonardo.cancel_element)
        self.dp.callback_query(F.data == 'cancel_element')(self.cancel)
        
        #self.dp.callback_query(Form.set_selement)        

    async def command_start_handler(self, message: Message):
        info = UserInfo(message)
        user_id = info.chat_id
        username = info.username
        language_code = info.language
        first_name = info.first_name
        referral = info.text
        db = Database()
        status = await info.get_user_member(user_id, self.bot)
        try:       
            now = datetime.now()
            total_token = db.user_token(user_id)       
            status = await info.get_vip_member(user_id, self.bot)
            if status == 'member' or status == 'creator':
                payed = db.get_payed_user(user_id)
                if payed is None:
                    total_token = total_token + 50
                    db.update_user_token(total_token, user_id)
                    db.insert_payed_user(user_id, now)
            parti = referral.split()
            
            mode = self.db.get_mode(user_id)
            keyboard = Keyboard_Manager().reply_add_token(mode)
            user = db.get_user_data(user_id)
            if user == None:
                if len(parti) > 1:
                    id_win_token = parti[1]  
                    total_token = db.user_token(id_win_token)
                    total_token = total_token + 4
                    db.update_user_token(total_token, id_win_token)
                    your_friend_joined = Language().your_friend_joined(language_code)
                    await self.bot.send_message(id_win_token, your_friend_joined)
                total_token += 0
                db.update_user_token(total_token, user_id)
                
            if status == 'member' or status == 'creator':
                new_member = db.get_member(user_id)
                if new_member == None:
                    total_token = total_token + 2
                    db.insert_member(user_id, True)
                    db.update_user_token(total_token, user_id)
            db.insert_user_data(user_id, username)                 
            
            text = Language().welcame(language_code, first_name, total_token)
            await message.answer(text, reply_markup=keyboard)
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex, exc_info=True)

    async def leonardo_ai(self, callback: CallbackQuery):
        info = UserInfo(callback)
        db = Database()
        user_id = info.user_id
        language_code = info.language
        first_name = info.first_name
        message_id = info.message_id
        mode = self.db.get_mode(user_id)
        mode = not mode
        try:
            # status = await info.get_vip_member(user_id, self.bot)
            # if status == 'member' or status == 'creator':
            self.db.insert_mode(user_id, mode)
            mode_on = "On ✅"
            mode_off = "Off 🚫"
            mode_on_off = mode_on if mode else mode_off
            await callback.answer(f"Mode setted to {mode_on_off}")
            keyboard = Keyboard_Manager().reply_add_token(leonardo=mode)
            total_token = db.user_token(user_id)
            text = Language().welcame(language_code, first_name, total_token)
            if mode:
                leonardo_ai = f'<a href="https://app.leonardo.ai/?via=Tasuboyz">Leonardo AI</a>'
                await callback.message.answer(f"Welcome to {leonardo_ai} Mode 🔥")
            await self.bot.edit_message_reply_markup(chat_id=user_id, message_id=message_id, reply_markup=keyboard)
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex, exc_info=True)

    async def give_referral(self, callback: CallbackQuery):
        info = UserInfo(callback)
        user_id = info.user_id
        language_code = info.language
        try:
            #test = f"`https://t.me/TasuAdmin_Bot?start={user_id}`"
            referral = f"`https://t.me/AIGenerativeTasuBot?start={user_id}`"      
            token_referral = Language().give_referral(language_code, referral)
            await callback.message.answer(text=token_referral, parse_mode=ParseMode.MARKDOWN)
            pass
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex, exc_info=True)

    async def recive_prompts(self, message: Message, state: FSMContext):        
        info = UserInfo(message)
        user_id = info.user_id
        chat_id = info.chat_id
        language_code = info.language
        db = Database()
        language = Language()
        try:
            if user_id in self.blocked_users:
                await self.bot.send_message(self.admin_id, f"{user_id}: Blocked")
                return
            total_token = db.user_token(user_id)
            if total_token > 1:
                mode = self.db.get_mode(user_id)
                if mode == False:
                    waiting = Language().waiting(language_code)
                    message_wait = await message.answer(waiting)
                    
                    prompt = message.text
                    prompt = re.sub(r'\(\d+\)$', '', prompt)

                    image_url = self.openai.prompt_to_image(prompt)         
                    self.blocked_users[user_id] = True            

                    keyboard = Keyboard_Manager().send_keyboard(language_code)
                    await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f'"`{prompt}`"\n(0)', reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
                    total_token -= 2
                    db.update_user_token(total_token, user_id)
                
                    if image_url:
                        await self.bot.delete_message(chat_id, message_wait.message_id) 
                else:
                    enable = db.get_enabled_mode(self.admin_id)
                    if enable:
                        vip_member = db.get_vip_member(user_id)
                        status = await info.get_vip_member(user_id, self.bot)
                        if status == 'member' or status == 'creator' or status == 'administrator':                                             
                            await self.leonardo.recive_prompt(message, state)
                        else:
                            if vip_member == None:
                                await self.leonardo.recive_prompt(message, state)
                            else:
                                you_not_vip = language.user_not_payed(language_code)
                                await message.answer(you_not_vip)
                    else:
                        await self.leonardo.recive_prompt(message, state)
            else:
                keyboard = Keyboard_Manager().buy_inline_keyboard()
                not_token = Language().have_not_token(language_code)
                await message.reply(not_token, reply_markup=keyboard)
                image_url = False
        except Exception as ex:
            error_occurred = Language().error_generation(language_code)
            await message.reply(error_occurred)
            logger.error(ex, exc_info=True)
            #await self.bot.send_message(self.admin_id, f"Errore {user_id}: {ex}")
        finally:
            if user_id in self.blocked_users:
                del self.blocked_users[user_id]
                
    async def info_of_contest(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        user_id = info.user_id      
        language_code = info.language
       
        db = Database()
        submission_time = db.get_first_submission_of_month()
        if submission_time is not None:
            submission_time = datetime.strptime(submission_time, '%Y-%m-%d %H:%M:%S')
            estimated_time = submission_time + timedelta(hours=self.contest_time)
            info_of_contest = Language().send_for_contest(language_code, estimated_time)
        else:
            info_of_contest = Language().send_for_contest_v2(language_code)
        
        keyboard = self.keyboard.yes_or_no(language_code)
        await self.bot.send_message(user_id, info_of_contest, reply_markup=keyboard)
        return

    async def send_image_to_channel(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        user_id = info.user_id      
        language_code = info.language
        db = Database()
        try:
            result = db.get_concurrent(user_id)
            if result:               
                submission_time = db.get_first_submission_of_month()
                submission_time = datetime.strptime(submission_time, '%Y-%m-%d %H:%M:%S')
                
                estimated_time = submission_time + timedelta(hours=self.contest_time)
                wait_next_text = Language().wait_for_next(language_code, estimated_time)
                await callback_query.message.reply(f"{wait_next_text}")
                return
            else:
                current_datetime = datetime.now()
                current_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                keyboard = Keyboard_Manager().star_keyboard()
                photo = await callback_query.message.send_copy(self.channel_id, reply_markup=keyboard)
                photo_id = photo.message_id
                channel_link = f'<a href="https://t.me/{self.channel_username}/{photo_id}">💣</a>'
                original = info.caption_text
                await callback_query.message.edit_caption(f''' ''')
                await callback_query.message.reply(f"Succesfully sended! {channel_link}")                   
                
                db.insert_concurrent(user_id, photo_id, current_datetime)
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex, exc_info=True)

    async def cancel(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        chat_id = info.chat_id
        message_id = info.message_id
        await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="🗑🗑🗑")
        
    async def choose_lang(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        messgae_id = info.message_id
        chat_id = info.chat_id
        keyboard = self.keyboard.language_setting()
        await self.bot.edit_message_text(text="Choose language:", chat_id=chat_id, message_id=messgae_id, reply_markup=keyboard)

    async def choosed_language(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        db = Database()
        user_id = info.user_id
        message_id = info.message_id
        data = info.user_data
        language_code = data.split(':')[1].strip()
        db.insert_language(user_id, language_code)
        language_setted = Language().language_setted(language_code)
        await self.bot.edit_message_text(text=f"{language_setted}",chat_id=user_id, message_id=message_id)