import config

from aiogram import F, Bot, Dispatcher, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
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
        #command
        self.dp.message(CommandStart())(self.command_start_handler)
        self.dp.message(F.text)(self.recive_prompts)
        self.dp.callback_query(F.data == "send")(self.info_of_contest)
        self.dp.callback_query(F.data == "1.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "2.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "3.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "4.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "5.0")(self.voting.give_star)
        self.dp.callback_query(F.data == "modify")(self.admin_panel.edit_to_markdown)
        self.dp.callback_query(F.data == "send_to_leonardo")(self.admin_panel.send_to_leonardo)
        self.dp.callback_query(F.data == "token")(self.give_referral)
        self.dp.callback_query(F.data == "yes")(self.send_image_to_channel)
        self.dp.callback_query(F.data == "cancel")(self.cancel)

        self.dp.message(F.from_user.id == self.admin_id)(self.admin_panel.admin_command)

    async def command_start_handler(self, message: Message):
        info = UserInfo(message)
        user_id = info.chat_id
        username = info.username
        language_code = info.language
        first_name = info.first_name
        referral = info.text
        status = await info.get_user_member(user_id, self.bot)
        try:              
            parti = referral.split()
            total_token = Database().user_token(user_id)
            keyboard = Keyboard_Manager().reply_add_token()
            user = Database().get_user_data(user_id)
            if user == None:
                if len(parti) > 1:
                    id_win_token = parti[1]  
                    total_token = Database().user_token(id_win_token)
                    total_token = total_token + 3
                    Database().update_user_token(total_token, id_win_token)
                    your_friend_joined = Language().your_friend_joined(language_code)
                    await self.bot.send_message(id_win_token, your_friend_joined)
                total_token += 1
                Database().update_user_token(total_token, user_id)
                
                if status == 'member' or status == 'creator':    
                    total_token = total_token + 2
                    Database().update_user_token(total_token, user_id)
            Database().insert_user_data(user_id, username)                 
            
            text = Language().welcame(language_code, first_name, total_token)
            await message.answer(text, reply_markup=keyboard)
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex)

    async def give_referral(self, callback: CallbackQuery):
        info = UserInfo(callback)
        user_id = info.user_id
        language_code = info.language
        test = f"`https://t.me/TasuAdmin_Bot?start={user_id}`"
        #referral = f"`https://t\\.me/AIGenerativeTasuBot\\?start={user_id}`"      
        token_referral = Language().give_referral(language_code, test)
        await callback.message.answer(text=token_referral, parse_mode=ParseMode.MARKDOWN)
        pass

    async def recive_prompts(self, message: Message):        
        info = UserInfo(message)
        user_id = info.user_id
        chat_id = info.chat_id
        language_code = info.language
        try:
            total_token = Database().user_token(user_id)
            if total_token > 0:
                
                waiting = Language().waiting(language_code)
                message_wait = await message.answer(waiting)
                
                prompt = message.text
                image_url = self.openai.prompt_to_image(prompt)                     

                keyboard = Keyboard_Manager().send_keyboard(language_code)
                await self.bot.send_photo(chat_id=user_id, photo=image_url, caption=f"`{prompt}`\n(0)", reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)
                total_token -= 1
                Database().update_user_token(total_token, user_id)
            else:
                keyboard = Keyboard_Manager().buy_inline_keyboard()
                not_token = Language().have_not_token(language_code)
                await message.reply(not_token, reply_markup=keyboard)
                image_url = False
        except Exception as ex:
            error_occurred = Language().error_generation(language_code)
            await message.reply(error_occurred)
            logger.error(ex)
            await self.bot.send_message(self.admin_id, f"Errore {user_id}: {ex}")
        finally:
            if image_url:
                await self.bot.delete_message(chat_id, message_wait.message_id) 

    async def info_of_contest(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        user_id = info.user_id      
        language_code = info.language
       
        db = Database()
        submission_time = db.get_first_submission_of_month()
        if submission_time is not None:
            submission_time = datetime.strptime(submission_time, '%Y-%m-%d %H:%M:%S.%f')
            estimated_time = submission_time + timedelta(hours=self.contest_time)
            info_of_contest = Language().send_for_contest(language_code, estimated_time)
        else:
            info_of_contest = Language().send_for_contest_v2(language_code)
        
        keyboard = self.keyboard.yes_or_no(language_code)
        await callback_query.message.answer(info_of_contest, reply_markup=keyboard)
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
                submission_time = datetime.strptime(submission_time, '%Y-%m-%d %H:%M:%S.%f')
                estimated_time = submission_time + timedelta(hours=self.contest_time)
                wait_next_text = Language().wait_for_next(language_code, estimated_time)
                await callback_query.message.reply(f"{wait_next_text}")
                return
            else:
                await self.execute_when_queue_clears(callback_query)
        except Exception as ex:
            await self.bot.send_message(self.admin_id, f"{ex}")
            logger.error(ex)

    async def execute_when_queue_clears(self, callback_query: CallbackQuery):
        db = Database()
        info = UserInfo(callback_query)
        user_id = info.user_id
        while True:          
            oldest_datetime = db.get_oldest_datetime()  # Assumendo che hai una funzione per ottenere la data più vecchia
            current_datetime = datetime.now()

            if oldest_datetime is not None:
                oldest_datetime = datetime.strptime(oldest_datetime, '%Y-%m-%d %H:%M:%S')  # Assumendo che le date nel tuo database siano in questo formato
                if (current_datetime - oldest_datetime) > timedelta(days=1):
                    db.clear_queue()
                    logger.info("Il database è stato resettato.")
                    continue
            queue_length = db.get_count_queue()
            if queue_length < 10:
                    current_datetime = datetime.now()
                    keyboard = Keyboard_Manager().star_keyboard()
                    photo = await callback_query.message.send_copy(self.channel_id, reply_markup=keyboard)
                    db.insert_queue(user_id, current_datetime)
                    photo_id = photo.message_id
                    channel_link = f'<a href="https://t.me/{self.channel_username}/{photo_id}">💣</a>'
                    original = info.caption_text
                    await callback_query.message.edit_caption(f''' ''')
                    await callback_query.message.reply(f"Succesfully sended! {channel_link}")                   
                    
                    db.insert_concurrent(user_id, photo_id, current_datetime)
                    break
            else:
                logger.error(f"Coda piena, ci sono {queue_length} azioni in coda. Riprovo tra 1 giorno.")
                time.sleep(86.400)  # Aspetta 1 giorno prima di riprovare

    async def cancel(self, callback_query: CallbackQuery):
        info = UserInfo(callback_query)
        chat_id = info.chat_id
        message_id = info.message_id
        await self.bot.edit_message_text(chat_id=chat_id, message_id=message_id, text="🗑🗑🗑")
        return